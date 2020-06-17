<html>

<head>
	<title>Hello Osones</title>
	<link href='//fonts.googleapis.com/css?family=Open+Sans:400,700' rel='stylesheet' type='text/css'>
	<style>
	body {
		background-color: white;
		text-align: center;
		padding: 50px;
		font-family: "Open Sans","Helvetica Neue",Helvetica,Arial,sans-serif;
	}

	#logo {
		margin-bottom: 40px;
	}
	</style>
</head>
<body>
	<img id="logo" src="logo.png" />
	<h1 style="color:green;"> Hello Osones </h1>
	<?php if($_ENV["HOSTNAME"]) {?><h3>My hostname is <?php echo $_ENV["HOSTNAME"]; ?></h3><?php } ?>
		</body>
</html>
