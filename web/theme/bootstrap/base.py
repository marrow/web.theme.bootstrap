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
	
	: scripts = ['//cdn.jsdelivr.net/g/jquery@1.11.3,bootstrap@3.3.5(js/bootstrap.js+js/bootstrap.min.js),jquery.cookie@1.4.1,fitvids@1.1.0'] + scripts
	: styles = ['//cdn.jsdelivr.net/fontawesome/4.4.0/css/font-awesome.min.css', '//cdn.jsdelivr.net/g/bootstrap@3.3.5(css/bootstrap.min.css+css/bootstrap-theme.min.css)'] + styles
	
	: return page_(title, header=header, footer=footer, metadata=metadata, styles=styles, scripts=scripts, **attributes)
: end
