
$(document).ready(function () {
    $("#id_submit").click(function (e){
        if ($("#id_username").val().length <= 5 || $("#id_username").val().length >=20){
            alert(" Login can not consist of less than five or more than twenty characters")
            e.preventDefault()
        }else if ($("#id_password").val().length <=5 || $("#id_password").val().length >= 20){
            alert("Password can not consist of less than five or more than twenty characters")
            e.preventDefault()
        }else if ($("#id_email").val().length ===0){
            alert("Please enter correct email")
            e.preventDefault()
        }else {
            alert("Register succes")
        }
    })

    $("#id_username").blur(function () {
     $.post(
            "check_login",
            {
                "username":$("#id_username").val()
            },
            function (response) {
                if (response.exist == 1) {
                    alert("This username already exist")
                }
            }
)})


})





