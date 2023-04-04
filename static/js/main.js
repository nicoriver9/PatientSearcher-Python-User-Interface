$(document).ready(function() {
    $("#myForm").submit(function(e) {
      e.preventDefault(); 
      document.getElementById('response').innerText = '';     
      const button = document.getElementById('my-button');
      const spinner = document.getElementById('spinner');

      // Hide the button and show the spinner
      button.classList.add('hidden');
      spinner.classList.remove('hidden');

      $.ajax({
        url: "http://127.0.0.1:5000",
        type: "post",
        data: $("#myForm").serialize(),
        success: function(response) {
          console.log( response.lentgh) 
          document.getElementById('response').innerText = response;              
          spinner.classList.add('hidden');
          button.classList.remove('hidden');
        },
        error: function(xhr) {
          console.log('erorrr' + xhr.responseText);
        }
      });
    });
  });