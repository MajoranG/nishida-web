class webConnector extends XMLHttpRequest {
    constructor() {
        super();
        this.addEventListener('loadstart', function () {
        }, false);
        this.addEventListener('load', function () {
            let data = this.response;
            if (data["mode"] == '!create')
                create_room(data);
            else if (data["mode"] == '!delete')
                delete_room(data);
            else if (data["mode"] == '!search')
                search_room(data);
            else if (data["mode"] == '!show')
                show_rooms(data);

        }, false);
        this.addEventListener('error', function () {
            window.alert(this.url + "と通信できません");
        }, false);
    }
}

let repeatR = function(){
    let xhr_r = new webConnector();
    let url_r = "/cgi-bin/chat/handle_chat.py?" + "n=" + "" + "&m=" + "!show";
    xhr_r.open("GET",url_r);
    xhr_r.responseType = 'json';
    xhr_r.url_r = url_r;
    xhr_r.send(null);
};


document.addEventListener('DOMContentLoaded', function (){
    repeatR();

    // ルーム作成ボタンenable disable
    document.getElementById('create_room').disabled = true;
    document.getElementById('new_room').addEventListener('keyup',function(){
        if (this.value.length < 1) {
            document.getElementById('create_room').disabled = true;
        }
        else {
            document.getElementById('create_room').disabled = false;
        }
    },false);
    document.getElementById('new_room').addEventListener('change',function(){
        if (this.value.length < 1) {
            document.getElementById('create_room').disabled = true;
        }
    },false);

    // ルーム削除ボタン同
    document.getElementById('delete_room').disabled = true;
    document.getElementById('deleting_room').addEventListener('keyup',function(){
        if (this.value.length < 1) {
            document.getElementById('delete_room').disabled = true;
        }
        else {
            document.getElementById('delete_room').disabled = false;
        }
    },false);
    document.getElementById('deleting_room').addEventListener('change',function(){
        if (this.value.length < 1) {
            document.getElementById('delete_room').disabled = true;
        }
    },false);
    
    // ルーム検索ボタン同
    document.getElementById('search_room').disabled = true;
    document.getElementById('searching_room').addEventListener('keyup',function(){
        if (this.value.length < 1) {
            document.getElementById('search_room').disabled = true;
        }
        else {
            document.getElementById('search_room').disabled = false;
        }
    },false);
    document.getElementById('searching_room').addEventListener('change',function(){
        if (this.value.length < 1) {
            document.getElementById('search_room').disabled = true;
        }
    },false);
    
    // ルーム作成(参加)
	let xhr = new webConnector();
	document.getElementById('create_room').addEventListener('click', function(){
        console.log('create');
		let name = document.getElementById('new_room').value;
        let url = "/cgi-bin/chat/handle_chat.py?" + "n=" + name + "&m=" + "!create";
		xhr.open("GET",url);
		xhr.responseType = 'json';
		xhr.url = url;
		xhr.send(null);
		
		document.getElementById('new_room').value = "";
		document.getElementById('create_room').disabled = true;
    },false);   
    
    // ルーム削除
	let xhr_d = new webConnector();
	document.getElementById('delete_room').addEventListener('click',function(){
        let name = document.getElementById('deleting_room').value;
		let url_d = "/cgi-bin/chat/handle_chat.py?" + "n=" + name + "&m=" + "!delete";
		xhr_d.open("GET",url_d);
        xhr_d.responseType = 'json';
        xhr_d.url_d = url_d;
        xhr_d.send(null);
    },false);
    
    // ルーム検索
    let xhr_s = new webConnector();
	document.getElementById('search_room').addEventListener('click',function(){
        let name = document.getElementById('searching_room').value;
		let url_s = "/cgi-bin/chat/handle_chat.py?" + "n=" + name + "&m=" + "!search";
		xhr_s.open("GET",url_s);
        xhr_s.responseType = 'json';
        xhr_s.url_s = url_s;
        xhr_s.send(null);
    },false);
},false);


//window.addEventListener('DOMContentLoaded',function(){
    
//},false);

function create_room(data){
    let result_name = [];
    //console.log(t_past);
    result_name = data["new_room"][0];
    window.location.href = '/chats/' + result_name + '.html';
}

function delete_room(data){
    let result_name = data["deleting_room"][0];
    let name = document.getElementById('deleting_room').value;
    //console.log(t_past);
    if (result_name == '') {
        window.alert(name + " does not exist.");
    } else {
        window.alert(name + " deleted.");
        document.getElementById('deleting_room').value = "";
        document.getElementById('delete_room').disabled = true;
        repeatR();
    }
}

function search_room(data){
    let result_name = data["searching_room"];
    let name = document.getElementById('searching_room').value;
    //console.log(t_past);
    if (result_name == null) {
        window.alert(name + " does not exist.");
    } else {
        window.alert(result_name + " exists.");
    }
}

function show_rooms(data){
	let content = document.getElementById('content');
    let result_name = [];
    let error = document.getElementById('error');
    //console.log(t_past);
    console.log(data);
    result_name = data["rooms"];
    content.innerHTML = ""
    for(let i = 0; i< result_name.length;i++){
        if (result_name[0] != '') {
            content.innerHTML = "<a href=/chats/" + result_name[i] + ".html>"+result_name[i] + "  </a><br />" + content.innerHTML;
        }
    
    }
}
