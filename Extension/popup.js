function transfer(){	
	var tablink;
	chrome.tabs.getSelected(null,function(tab) {
	   	tablink = tab.url;
		$("#p1").text("The URL being tested is - "+tablink);

		var xhr=new XMLHttpRequest();
		params="url="+tablink;
//		alert(params);
		var markup = "url="+tablink+"&html="+document.documentElement.innerHTML;
		xhr.open("POST","http://localhost:8000/check/",false);
		xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xhr.send(markup);
//		alert(xhr.responseText);

		response = xhr.responseText.replace(/^\s*/,'').replace(/\s*$/,'')
		$("#div1").text(response);
		if(xhr.responseText == "SAFE")
		{
			document.getElementById('div1').style.color = "#55ba57";
		}
		else
		{
			document.getElementById('div1').style.color = "#e85c35";
		}
		return xhr.responseText;
	});
}

$(document).ready(function(){
    $("button").click(function(){
		$("div#div1").show();	
		return transfer();
    });
});

chrome.tabs.getSelected(null,function(tab) {
   	var tablink = tab.url;
	$("#p1").text("The URL being tested is - "+tablink);
});
