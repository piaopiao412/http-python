<?
$value1 = $_POST["name"];
$value2 = $_POST["age"];

move_upload_file($_FILES["file1"]["tmp_name"];
	$_SERVER["DOCUMENT_ROOT]."/uploadFiles/" .$_FILES["file1"]["name"]);
	
move_upload_file($_FILES["file2"]["tmp_name"];
	$_SERVER["DOCUMENT_ROOT]."/uploadFiles/" .$_FILES["file2"]["name"]);
?>
