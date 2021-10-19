
if (document.readyState == 'loading') {
  document.addEventListener('DOMContentLoaded', ready)
} else {
  ready()
}

function ready() {
  
  document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.carousel');
    var instances = M.Carousel.init(elems, {
      fullWidth: true,
      indicators: true
    });
  });
  
  document.addEventListener('DOMContentLoaded', function () {
    const optionsModal = {
      onOpenStart: () => {
        $('.warning-msg').text(" ")
        $('.success-msg').text(" ")
        $('input').removeClass("invalid valid")
        $('input').val("")
      }
    }
    var elems = document.querySelectorAll('.modal');
    var instance = M.Modal.init(elems, optionsModal);
  });
}


$(document).ready(function () {
  console.log("js loaded");
  let email = "";
  let password = "";

  $('#login-form').change(function () {
    email = $('#email').val();
    password = $('#password').val();
  });
  $('#login-form').submit(function (e) {
    e.preventDefault();

    $.ajax({
      url: "/login",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify({
        email: email,
        password: password
      }),
      success: function (data, __statusCode) {
        console.log(data);


        if (!data.success) {
          $('#password').val("")
          $('.warning-msg').text("Invalid email or password")
        } else {
          $('.warning-msg').text(" ")
          $('.success-msg').text("Logged in successfully")
          window.localStorage.setItem('email', data.email);
          const instance = M.Modal.getInstance(document.getElementById("modal-login"))
          setTimeout(() => {
            window.location.href = `${window.location.pathname}`;
            instance.close()
          }, 600)

        }
      },
      error: function (__xhr, __statusCode, error) {
        console.log(error);
      }
    });
  });

  $('#register-form').submit(function (e) {
    e.preventDefault();

    if ($('#user-password').val() === $('#password-confirmation').val()) {
      $.ajax({
        url: "/register",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({
          email: $('#user-email').val(),
          password: $('#user-password').val(),
          firstname: $('#first_name').val(),
          lastname: $('#last_name').val(),
          phone: $('#phone-number').val()
        }),
        success: function (data, __statusCode) {
          console.log(data);

          if (!data.success) {
            $('#user-email').addClass("invalid")
            $('.warning-msg').text("Email is invalid or already existed")
          } else {
            $('.warning-msg').text(" ")
            $('.success-msg').text("Registered successfully")
            const instance = M.Modal.getInstance(document.getElementById("modal-signup"))
            setTimeout(() => instance.close(), 2000)

          }
        },
        error: function (__xhr, __statusCode, error) {
          console.log(error);
        }
      });
    } else {
      $('#user-password').addClass("invalid")
      $('#password-confirmation').addClass("invalid")
      $('.warning-msg').text("invalid password")
    }

  });

});