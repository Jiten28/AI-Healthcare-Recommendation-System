function togglePassword(inputId, icon){

    const input=document.getElementById(inputId);

    if(input.type==="password"){

        input.type="text";

        icon.classList.replace("bi-eye-slash","bi-eye");

    }else{

        input.type="password";

        icon.classList.replace("bi-eye","bi-eye-slash");

    }

}

const password=document.getElementById("password");

if(password){

password.addEventListener("input",()=>{

const value=password.value;

const fill=document.getElementById("strength-fill");

const text=document.getElementById("strength-text");

let strength=0;

if(value.length>=8) strength++;

if(/[A-Z]/.test(value)) strength++;

if(/[0-9]/.test(value)) strength++;

if(/[!@#$%^&*]/.test(value)) strength++;

switch(strength){

case 1:

fill.style.width="25%";
fill.style.background="#ef4444";
text.innerHTML="Weak Password";
break;

case 2:

fill.style.width="50%";
fill.style.background="#f59e0b";
text.innerHTML="Medium Password";
break;

case 3:

fill.style.width="75%";
fill.style.background="#3b82f6";
text.innerHTML="Strong Password";
break;

case 4:

fill.style.width="100%";
fill.style.background="#22c55e";
text.innerHTML="Very Strong Password";
break;

default:

fill.style.width="0%";
text.innerHTML="Password Strength";

}

});

}