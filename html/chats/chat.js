class webConnector extends XMLHttpRequest {
    constructor() {
        super();
        this.addEventListener('loadstart', function () {
        }, false);
        this.addEventListener('load', function () {
            let data = this.response;
            if (data["your_id"] != null && document.getElementById('id').innerHTML == '') {
                id = data["your_id"];
                document.getElementById('id').innerHTML = 'あなたのID: ' + id;
            }
            showLog(data);
        }, false);
        this.addEventListener('error', function () {
            window.alert(this.url + "と通信できません");
        }, false);
    }
}

let id;
let get_id = function(){
    let xhr_a = new webConnector();
    let url_a = "/cgi-bin/chat/chat.py?" + "n=" + "!id" + "&m=" + "!id" + "&o=" + "!id";
    xhr_a.open("GET",url_a);
    xhr_a.responseType = 'json';
    xhr_a.url_a = url_a;
    xhr_a.send(null);
};

document.addEventListener('DOMContentLoaded', function (){
    get_id();

    // 通知の許可
    (function() {
        if ("Notification" in window) {
          var permission = Notification.permission;
      
          if (permission === "denied" || permission === "granted") {
            return;
          }
        }
      })();


    document.getElementById('submit').disabled = true;
    document.getElementById('message').addEventListener('keyup',function(){
        if (this.value.length < 1) {
            document.getElementById('submit').disabled = true;
        }
        else {
            document.getElementById('submit').disabled = false;
        }
    },false);
    document.getElementById('message').addEventListener('change',function(){
        if (this.value.length < 1) {
            document.getElementById('submit').disabled = true;
        }
    },false);
	
	document.getElementById('message').addEventListener('keypress', function(e){
		if(e.keyCode === 13){
			document.getElementById('submit').click();
		}
	},false);   

	let xhr = new webConnector();
	
	document.getElementById('submit').addEventListener('click', function(){
		let name = document.getElementById('name').value;
        let message = document.getElementById('message').value;
        let url = "/cgi-bin/chat/chat.py?" + "n=" + name + "&m=" + message + "&o=" + room_name;
		xhr.open("GET",url);
		xhr.responseType = 'json';
		xhr.url = url;
		xhr.send(null);
		
		document.getElementById('message').value = "";
		document.getElementById('submit').disabled = true;
    },false);

    let xhr_r = new webConnector();
    let repeatR = function(){
        let url_r = "/cgi-bin/chat/chat.py?" + "n=" + "!reload" + "&m=" + "!reload" + "&o=" + room_name;
        xhr_r.open("GET",url_r);
        xhr_r.responseType = 'json';
        xhr_r.url_r = url_r;
        xhr_r.send(null);
    };
    repeatR();
    setInterval(repeatR,10000);
	
	let xhr_d = new webConnector();
	document.getElementById('delete').addEventListener('click',function(){
		let url_d = "/cgi-bin/chat/chat.py?" + "n=" + "!delete" + "&m=" + "!delete" + "&o=" + room_name;
		xhr_d.open("GET",url_d);
        xhr_d.responseType = 'json';
        xhr_d.url_d = url_d;
        xhr_d.send(null);
	},false);
    
},false);

//window.addEventListener('DOMContentLoaded',function(){
    
//},false);
let j = 1;  // レス番号
let last_message = "";
let t_past = 0;
function showLog(data){
	let content = document.getElementById('content');
    let error = document.getElementById('error');
    let l;
    //console.log(t_past);
    if (data === null) {
        //content.textContent = 'NO CONTENT';
        //error.textContent = 'メッセージまたは名前が入力されていません';
    } else {
        l = data["utime"].length;
        
        for(let i = 0; i<l; i++){
            if(data["utime"][i] > t_past){
                if (data["id"][i] == 'NSD') {
                    content.innerHTML = 'NSD: ' + data["name"][i]+"("+data["id"][i]+"):  "+data["message"][i]+" ("+data["time"][i]+")</br>"+content.innerHTML;
                }
                else {
                    if (id == data["id"][i])                        
                        content.innerHTML = "<b>" + String(j) + '</b>: ' + data["name"][i]+"("+data["id"][i]+"):  "+data["message"][i]+" ("+data["time"][i]+")</br>"+content.innerHTML;
                    else 
                        content.innerHTML = String(j) + ': ' + data["name"][i]+"("+data["id"][i]+"):  "+data["message"][i]+" ("+data["time"][i]+")</br>"+content.innerHTML;
                    j++;
                }
            }            
        }
        let now_last_message = data["name"][l-1]+data["id"][l-1]+data["message"][l-1]+data["time"][l-1]
        if(last_message != now_last_message && id != data["id"][l-1] && data["id"][l-1] != 'NSD') {
            Notification
            .requestPermission()
            .then(function() {
                var notification = new Notification(data["name"][l-1]+"("+data["id"][l-1]+"):"+data["message"][l-1]);
            });            
        }
        last_message = now_last_message;
        t_past = data["utime"][l-1];
    }
}

