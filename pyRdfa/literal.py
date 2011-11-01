# -*- coding: utf-8 -*-
"""
Implementation of the Literal handling. Details of the algorithm are described on
U{RDFa Task Force's wiki page<http://www.w3.org/2006/07/SWD/wiki/RDFa/LiteralObject>}.

@summary: RDFa Literal generation
@requires: U{RDFLib package<http://rdflib.net>}
@organization: U{World Wide Web Consortium<http://www.w3.org>}
@author: U{Ivan Herman<a href="http://www.w3.org/People/Ivan/">}
@license: This software is available for use under the
U{W3C® SOFTWARE NOTICE AND LICENSE<href="http://www.w3.org/Consortium/Legal/2002/copyright-software-20021231">}
"""

"""
$Id: literal.py,v 1.2 2011/09/16 12:26:02 ivan Exp $
$Date: 2011/09/16 12:26:02 $
"""

import re

import rdflib
from rdflib	import BNode
from rdflib	import Literal, URIRef, Namespace
if rdflib.__version__ >= "3.0.0" :
	from rdflib	import RDF as ns_rdf
else :
	from rdflib.RDF	import RDFNS as ns_rdf

from pyRdfa	import IncorrectBlankNodeUsage, err_no_blank_node, ns_xsd 
from pyRdfa.utils import has_one_of_attributes

XMLLiteral = ns_rdf["XMLLiteral"]

class ProcessProperty :
	"""Generate the value for C{@property} taking into account datatype, etc.
	Note: this class is created only if the C{@property} is indeed present, no need to check. 
	
	@ivar node: DOM element node
	@ivar graph: the (RDF) graph to add the properies to
	@ivar subject: the RDFLib URIRef serving as a subject for the generated triples
	@ivar state: the current state to be used for the CURIE-s
	@type state: L{state.ExecutionContext}
	"""
	def __init__(self, node, graph, subject, state) :
		self.node    = node
		self.graph   = graph
		self.subject = subject
		self.state   = state
		
	def generate(self) :
		if self.state.rdfa_version >= "1.1" :
			self.generate_1_1()
		else :
			self.generate_1_0()
	
	def generate_1_1(self) :
		"""Generate the property object, 1.1 version"""
		
		object = None
				
		#########################################################################		
		# See if the target is _not_ a literal
		irirefs = ("resource", "href", "src")
		noiri = ("content", "datatype", "rel", "rev")
		if has_one_of_attributes(self.node, irirefs) and not has_one_of_attributes(self.node, noiri ) :
			if self.node.hasAttribute("resource") :
				object = self.state.getURI("resource")
			elif self.node.hasAttribute("href") :
				object = self.state.getURI("href")
			elif node.hasAttribute("src") :
				object = self.state.getURI("src")
		else :
			# We have to generate a literal indeed.
			# Get, if exists, the value of @datatype
			datatype = ''
			dtset    = False
			if self.node.hasAttribute("datatype") :
				dtset = True
				dt = self.node.getAttribute("datatype")
				if dt != "" :
					datatype = self.state.getURI("datatype")
		
			if self.state.lang != None :
				lang = self.state.lang
			else :
				lang = ''
	
			# The simple case: separate @content attribute
			if self.node.hasAttribute("content") :
				val = self.node.getAttribute("content")
				# Handling the automatic uri conversion case
				if dtset == False :
					object = Literal(val, lang=lang)
				else :
					object = self._create_Literal(val, datatype=datatype, lang=lang)
				# The value of datatype has been set, and the keyword paramaters take care of the rest
			else :
				# see if there *is* a datatype (even if it is empty!)
				if dtset :
					if datatype == XMLLiteral :
						object = Literal(self._get_XML_literal(self.node),datatype=XMLLiteral)
					else :
						object = self._create_Literal(self._get_literal(self.node), datatype=datatype, lang=lang)
				else :
					object = self._create_Literal(self._get_literal(self.node), lang=lang)
	
		if object != None :
			for prop in self.state.getURI("property") :
				if not isinstance(prop, BNode) :
					if self.state.rdfa_version >= "1.1" and self.node.hasAttribute("inlist") :
						self.state.add_to_list_mapping(prop, object)
					else :			
						self.graph.add( (self.subject, prop, object) )
				else :
					self.state.options.add_warning(no_blank_node % "property", warning_type=IncorrectBlankNodeUsage, node=self.node.nodeName)
	
		# return


	def generate_1_0(self) :
		"""Generate the property object, 1.0 version"""
				
		#########################################################################		
		# We have to generate a literal indeed.
		# Get, if exists, the value of @datatype
		datatype = ''
		dtset    = False
		if self.node.hasAttribute("datatype") :
			dtset = True
			dt = self.node.getAttribute("datatype")
			if dt != "" :
				datatype = self.state.getURI("datatype")
	
		if self.state.lang != None :
			lang = self.state.lang
		else :
			lang = ''

		# The simple case: separate @content attribute
		if self.node.hasAttribute("content") :
			val = self.node.getAttribute("content")
			# Handling the automatic uri conversion case
			if dtset == False :
				object = Literal(val, lang=lang)
			else :
				object = self._create_Literal(val, datatype=datatype, lang=lang)
			# The value of datatype has been set, and the keyword paramaters take care of the rest
		else :
			# see if there *is* a datatype (even if it is empty!)
			if dtset :
				# yep. The Literal content is the pure text part of the current element:
				# We have to check whether the specified datatype is, in fact, an
				# explicit XML Literal
				if datatype == XMLLiteral :
					object = Literal(self._get_XML_literal(self.node),datatype=XMLLiteral)
				else :
					object = self._create_Literal(self._get_literal(self.node), datatype=datatype, lang=lang)
			else :
				# no controlling @datatype. We have to see if there is markup in the contained
				# element
				if True in [ n.nodeType == self.node.ELEMENT_NODE for n in self.node.childNodes ] :
					# yep, and XML Literal should be generated
					object = self._create_Literal(self._get_XML_literal(self.node), datatype=XMLLiteral)
				else :
					# At this point, there might be entities in the string that are returned as real characters by the dom
					# implementation. That should be turned back
					object = self._create_Literal(self._get_literal(self.node), lang=lang)
	
		for prop in self.state.getURI("property") :
			if not isinstance(prop,BNode) :
				self.graph.add( (self.subject,prop,object) )
			else :
				self.state.options.add_warning(no_blank_node % "property", warning_type=IncorrectBlankNodeUsage, node=self.node.nodeName)
	
		# return
	
	######################################################################################################################################
	
	
	def _putBackEntities(self, str) :
		"""Put 'back' entities for the '&','<', and '>' characters, to produce kosher XML string.
		Used by XML Literal
		@param str: string to be converted
		@return: string with entities
		@rtype: string
		"""
		return str.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
		
	def _get_literal(self, Pnode):
		"""
		Get (recursively) the full text from a DOM Node.
	
		@param Pnode: DOM Node
		@return: string
		"""
		rc = ""
		for node in Pnode.childNodes:
			if node.nodeType == node.TEXT_NODE:
				rc = rc + node.data
			elif node.nodeType == node.ELEMENT_NODE :
				rc = rc + _get_literal(node)
	
		# The decision of the group in February 2008 is not to normalize the result by default.
		# This is reflected in the default value of the option		
		
		if self.state.options.space_preserve :
			return rc
		else :
			return re.sub(r'(\r| |\n|\t)+'," ",rc).strip()
	# end getLiteral
	
	def _get_XML_literal(self, Pnode) :
		"""
		Get (recursively) the XML Literal content of a DOM Node. (Most of the processing is done
		via a C{node.toxml} call of the xml minidom implementation.)
	
		@param Pnode: DOM Node
		@return: string
		"""
					
		rc = ""		
		for node in Pnode.childNodes:
			if node.nodeType == node.TEXT_NODE:
				rc = rc + self._putBackEntities(node.data)
			elif node.nodeType == node.ELEMENT_NODE :
				# Decorate the element with namespaces and lang values
				#for prefix in prefixes :
				#	if prefix in state.term_or_curie.xmlns and not node.hasAttribute("xmlns:%s" % prefix) :
				#		node.setAttribute("xmlns:%s" % prefix,"%s" % state.term_or_curie.xmlns[prefix])
				for prefix in self.state.term_or_curie.xmlns :
					if not node.hasAttribute("xmlns:%s" % prefix) :
						node.setAttribute("xmlns:%s" % prefix,"%s" % self.state.term_or_curie.xmlns[prefix])
				# Set the default namespace, if not done (and is available)
				if not node.getAttribute("xmlns") and self.state.defaultNS != None :
					node.setAttribute("xmlns", self.state.defaultNS)
				# Get the lang, if necessary
				if not node.getAttribute("xml:lang") and self.state.lang != None :
					node.setAttribute("xml:lang", self.state.lang)
				rc = rc + node.toxml()
		return rc
	# end getXMLLiteral
	
	def _create_Literal(self, val, datatype = '', lang = '') :
		"""
		Create a literal, taking into account the datatype and language.
		@return: Literal
		"""
		if datatype == None or datatype == '' :
			return Literal(val, lang=lang)
		#elif datatype == ns_xsd["string"] :
		#	return Literal(val)
		else :
			return Literal(val, datatype=datatype)

