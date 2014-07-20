/*amindhabitaciones*/
function addHabitacion(){
	var data = {
		'name' : document.querySelector('#nombreHabitacion').value
	}
	$.post('/addHabitacion', data, function(response) {
		if( response == 'not-login' )
			window.location = "/";
		else
			document.querySelector('.main').innerHTML=response
	
	});
}
/*Habitaciones*/
function loadAdminHabitaciones(){
	var data = {
	}
	$.post('/adminHabitaciones	', data, function(response) {
		if( response == 'not-login' )
			window.location = "/";
		else
			document.querySelector('.main').innerHTML=response
	
	});
}

/*login*/
function login(){
	$(password)[0].value = md5($(password)[0].value);
}	

/*body */
function selectOption(event) {
	$('.nav.nav-sidebar')[0].getElementsByClassName('active')[0].className=''
	event.toElement.parentElement.className='active'
}

function loadHabitacion(id){
	var data = {
		'id' : id
	}
	$.post('/habitacion', data, function(response) {
		if( response == 'not-login' )
			window.location = "/";
		else
			document.querySelector('.main').innerHTML = response;
	});
}
function go_to(){
	var data = {
	}
	$.post('/inicio', data, function(response) {
		if( response == 'not-login' )
			window.location = "/";
		else
			document.querySelector('.main').innerHTML = response;
	});
}

/*inicio*/

function startTime(){
	today=new Date();
	h=today.getHours();
	m=today.getMinutes();
	s=today.getSeconds();
	m=checkTime(m);
	if (document.getElementById('reloj'))
		document.getElementById('reloj').innerHTML=h+":"+m;
	t=setTimeout('startTime()',500);
}
function checkTime(i){
	if (i<10){
		i="0" + i;
	}
	return i;
}
window.onload=function(){startTime();}