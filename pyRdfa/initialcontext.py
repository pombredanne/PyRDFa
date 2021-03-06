# -*- coding: utf-8 -*-
"""
Built-in version of the initial contexts for RDFa Core, and RDFa + HTML

@summary: Management of vocabularies, terms, and their mapping to URI-s.
@requires: U{RDFLib package<http://rdflib.net>}
@organization: U{World Wide Web Consortium<http://www.w3.org>}
@author: U{Ivan Herman<a href="http://www.w3.org/People/Ivan/">}
@license: This software is available for use under the
U{W3C® SOFTWARE NOTICE AND LICENSE<href="http://www.w3.org/Consortium/Legal/2002/copyright-software-20021231">}

@var initial_context: dictionary for all the initial context data, keyed through the context URI-s
"""

"""
$Id: initialcontext.py,v 1.2 2011/11/14 14:02:48 ivan Exp $
$Date: 2011/11/14 14:02:48 $
"""

class Wrapper :
	pass
	
initial_context = {
	"http://www.w3.org/2011/rdfa-context/rdfa-1.1" 		: Wrapper(),
	"http://www.w3.org/2011/rdfa-context/html-rdfa-1.1" : Wrapper(),
}

initial_context["http://www.w3.org/2011/rdfa-context/rdfa-1.1"].ns = {
	'owl'		: 'http://www.w3.org/2002/07/owl#',
	'gr'		: 'http://purl.org/goodrelations/v1#',
	'ctag'		: 'http://commontag.org/ns#',
	'cc'		: 'http://creativecommons.org/ns#',
	'grddl'		: 'http://www.w3.org/2003/g/data-view#',
	'rif'		: 'http://www.w3.org/2007/rif#',
	'sioc'		: 'http://rdfs.org/sioc/ns#',
	'skos'		: 'http://www.w3.org/2004/02/skos/core#',
	'xml'		: 'http://www.w3.org/XML/1998/namespace',
	'rdfs'		: 'http://www.w3.org/2000/01/rdf-schema#',
	'rev'		: 'http://purl.org/stuff/rev#',
	'rdfa'		: 'http://www.w3.org/ns/rdfa#',
	'dc'		: 'http://purl.org/dc/terms/',
	'foaf'		: 'http://xmlns.com/foaf/0.1/',
	'void'		: 'http://rdfs.org/ns/void#',
	'ical'		: 'http://www.w3.org/2002/12/cal/icaltzd#',
	'vcard'		: 'http://www.w3.org/2006/vcard/ns#',
	'wdrs'		: 'http://www.w3.org/2007/05/powder-s#',
	'og'		: 'http://ogp.me/ns#',
	'wdr'		: 'http://www.w3.org/2007/05/powder#',
	'rdf'		: 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
	'xhv'		: 'http://www.w3.org/1999/xhtml/vocab#',
	'xsd'		: 'http://www.w3.org/2001/XMLSchema#',
	'v'			: 'http://rdf.data-vocabulary.org/#',
	'skosxl'	: 'http://www.w3.org/2008/05/skos-xl#',
	'schema'	: 'http://schema.org/',
}

initial_context["http://www.w3.org/2011/rdfa-context/rdfa-1.1"].terms = {
	'describedby'	: 'http://www.w3.org/2007/05/powder-s#describedby',
}

initial_context["http://www.w3.org/2011/rdfa-context/rdfa-1.1"].vocabulary = ""

initial_context["http://www.w3.org/2011/rdfa-context/html-rdfa-1.1"].ns = {
}

initial_context["http://www.w3.org/2011/rdfa-context/html-rdfa-1.1"].vocabulary = ""

initial_context["http://www.w3.org/2011/rdfa-context/html-rdfa-1.1"].terms = {
	'alternate'				: 'http://www.w3.org/1999/xhtml/vocab#alternate',
	'appendix'				: 'http://www.w3.org/1999/xhtml/vocab#appendix',
	'archives'				: 'http://www.w3.org/1999/xhtml/vocab#archives',
	'author'				: 'http://www.w3.org/1999/xhtml/vocab#author',
	'bookmark'				: 'http://www.w3.org/1999/xhtml/vocab#bookmark',
	'canonical'				: 'http://www.w3.org/1999/xhtml/vocab#canonical',
	'chapter'				: 'http://www.w3.org/1999/xhtml/vocab#chapter',
	'contents'				: 'http://www.w3.org/1999/xhtml/vocab#contents',
	'copyright'				: 'http://www.w3.org/1999/xhtml/vocab#copyright',
	'current'				: 'http://www.w3.org/1999/xhtml/vocab#current',
	'duplicate'				: 'http://www.w3.org/1999/xhtml/vocab#duplicate',
	'edit'					: 'http://www.w3.org/1999/xhtml/vocab#edit',
	'edit-media'			: 'http://www.w3.org/1999/xhtml/vocab#edit-media',
	'enclosure'				: 'http://www.w3.org/1999/xhtml/vocab#enclosure',
	'first'					: 'http://www.w3.org/1999/xhtml/vocab#first',
	'glossary'				: 'http://www.w3.org/1999/xhtml/vocab#glossary',
	'help'					: 'http://www.w3.org/1999/xhtml/vocab#help',
	'hub'					: 'http://www.w3.org/1999/xhtml/vocab#hub',
	'icon'					: 'http://www.w3.org/1999/xhtml/vocab#icon',
	'index'					: 'http://www.w3.org/1999/xhtml/vocab#index',
	'last'					: 'http://www.w3.org/1999/xhtml/vocab#last',
	'latest-version'		: 'http://www.w3.org/1999/xhtml/vocab#latest-version',
	'license'				: 'http://www.w3.org/1999/xhtml/vocab#license',
	'lrdd'					: 'http://www.w3.org/1999/xhtml/vocab#lrdd',
	'monitor'				: 'http://www.w3.org/1999/xhtml/vocab#monitor',
	'monitor-group'			: 'http://www.w3.org/1999/xhtml/vocab#monitor-group',
	'next'					: 'http://www.w3.org/1999/xhtml/vocab#next',
	'next-archive'			: 'http://www.w3.org/1999/xhtml/vocab#next-archive',
	'nofollow'				: 'http://www.w3.org/1999/xhtml/vocab#nofollow',
	'noreferrer'			: 'http://www.w3.org/1999/xhtml/vocab#noreferrer',
	'payment'				: 'http://www.w3.org/1999/xhtml/vocab#payment',
	'predecessor-version'	: 'http://www.w3.org/1999/xhtml/vocab#predecessor-version',
	'prefetch'				: 'http://www.w3.org/1999/xhtml/vocab#prefetch',
	'prev'					: 'http://www.w3.org/1999/xhtml/vocab#prev',
	'previous'				: 'http://www.w3.org/1999/xhtml/vocab#previous',
	'prev-archive'			: 'http://www.w3.org/1999/xhtml/vocab#prev-archive',
	'related'				: 'http://www.w3.org/1999/xhtml/vocab#related',
	'replies'				: 'http://www.w3.org/1999/xhtml/vocab#replies',
	'search'				: 'http://www.w3.org/1999/xhtml/vocab#search',
	'section'				: 'http://www.w3.org/1999/xhtml/vocab#section',
	'self'					: 'http://www.w3.org/1999/xhtml/vocab#self',
	'service'				: 'http://www.w3.org/1999/xhtml/vocab#service',
	'start'					: 'http://www.w3.org/1999/xhtml/vocab#start',
	'stylesheet'			: 'http://www.w3.org/1999/xhtml/vocab#stylesheet',
	'subsection'			: 'http://www.w3.org/1999/xhtml/vocab#subsection',
	'successor-version'		: 'http://www.w3.org/1999/xhtml/vocab#successor-version',
	'tag'					: 'http://www.w3.org/1999/xhtml/vocab#tag',
	'up'					: 'http://www.w3.org/1999/xhtml/vocab#up',
	'version-history'		: 'http://www.w3.org/1999/xhtml/vocab#version-history',
	'via'					: 'http://www.w3.org/1999/xhtml/vocab#via',
	'working-copy'			: 'http://www.w3.org/1999/xhtml/vocab#working-copy',
	'working-copy-of'		: 'http://www.w3.org/1999/xhtml/vocab#working-copy-of',

	'p3pv1'					: 'http://www.w3.org/1999/xhtml/vocab#p3pv1',
	'transformation'		: 'http://www.w3.org/2003/g/data-view#transformation',
	'itsRules'				: 'http://www.w3.org/1999/xhtml/vocab#itsRules',
	'role'					: 'http://www.w3.org/1999/xhtml/vocab#role',
}

