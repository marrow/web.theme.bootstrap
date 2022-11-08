# encoding: cinje

: from cinje.std.html import page as page_, default_header, default_footer


: def bootstrap_header title, metadata=[], styles=[], scripts=[]
	: """Prepare and generate the HTML <head> section."""
		
	: use default_header title, metadata=metadata, styles=styles, scripts=scripts
		
		<!--[if lt IE 9 ]>
		<script src="//cdn.jsdelivr.net/html5shiv/3.7.2/html5shiv-printshiv.min.js"></script>
		<script src="//cdn.jsdelivr.net/respond/1.4.2/respond.min.js"></script>
		<![endif]-->
: end


: def page context, title, header=bootstrap_header, footer=default_footer, metadata=[], styles=[], scripts=[], **attributes
	: """A general HTML page."""
	
	
	
	
	: scripts = ['https://cdn.jsdelivr.net/combine/npm/jquery@1.12.4,npm/bootstrap@3.4.1/dist/js/bootstrap.min.js,npm/jquery.cookie@1.4.1,npm/fitvids.js@1.2.0,npm/sortablejs@1.15.0,npm/imagesloaded@4.1.4'] + scripts
	: styles = ['//cdn.jsdelivr.net/fontawesome/4.7.2/css/font-awesome.min.css', 'https://cdn.jsdelivr.net/combine/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css,npm/bootstrap@3.4.1/dist/css/bootstrap-theme.min.css'] + styles
	
	: return page_(title, header=header, footer=footer, metadata=metadata, styles=styles, scripts=scripts, **attributes)
: end
