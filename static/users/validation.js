var error = document.getElementById("error")
var password;
function validate_name(object){
    document.getElementById("create").disabled = true
    let name = object.value;
    let re = /^[a-z]+$/i.test(name);
    if(re===false){
        var er = `${object.id} should contain only alphabets`
        error.innerHTML = er
    }else{
        error.innerHTML = ""
    }
    if(name.length>150){
        var er = `${object.id} should be less than 150 characters`
        error.innerHTML = er
    }else{
        error.innerHTML = " "
    }
}
function validate_username(object){
    let name = object.value;
    let re = /^[a-z0-9]+$/i.test(name);
    if(re===false){
        error.innerHTML = "Username can contain only alphanumeric characters"
    }else{
        error.innerHTML = "";
    }
    if(name.length>150){
        error.innerHTML = "Username should be less than 150 character"
    }else{
        error.innerHTML = "";
    }
}

function validate_email(object){
    let email = object.value
    let re = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email);
    if(re===false){
        error.innerHTML = "Invalid Email"
    }else{
        error.innerHTML = "";
    }
}

function validate_password(object){
    password = object.value;
    if(password.length<=8){
        error.innerHTML = "Password should be contain more than 8 characters"
    }else{
        error.innerHTML = "";
    }
}

function validate_confirm_password(object){
    let password1 = object.value;
    if(password1!=password){
        error.innerHTML = "Passwords does not matched"
    }else{
        error.innerHTML = "";
    }
}

function enable_submit(object){
    let pin_code = object.value
    if(pin_code.length==6)
    document.getElementById("create").disabled = false;
    else
    error.innerHTML = "Pincode should be 6 digits"
}