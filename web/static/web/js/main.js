(function(window, document, $){
  'use_strict';
  var app = {};


  app.getFormData = function(form) {
    var data = {}
    $.each(form.serializeArray(), function(ind, val){
      data[val.name] = val.value
    })
    return data;
  };

  app.getUserTime = function(userTime) {
    var hm = userTime.split(':');
    var hours = parseInt(hm[0]);
    var minutes = parseInt(hm[1]);
    var currentTime = new Date();
    return Date(currentTime.getFullYear(), currentTime.getMonth(), currentTime.getDay(), hours, minutes, 0, 0);
  };

  app.logAPI = function(url, email) {
    var currentTime = new Date().toLocaleTimeString();
    var log = "<p>["+ currentTime + "]" + " Requested " + url + " For [" + email +"]</p>"
    $("div#log").append(log);
  }

  

  $("#reminder").submit(function(e) {
    var uberAPI = $(this).data('uber');
    var mapsAPI = $(this).data('maps');
    var emailAPI = $(this).data('email');
    var data = app.getFormData($(this));
    var uberData = {'lat': data['slat'], 'long': data['slon']};
    var mapsData = {
      'slat': data['slat'], 'slon': data['slon'],
      'elat': data['elat'], 'elon': data['elon'],
    };
    var emailData = {'email': data['email']}
    function apiCalls() {
      currentTime = new Date().getTime();
      userTime = app.getUserTime(data['time'])
      remainingTime = userTime - currentTime;
      app.logAPI(uberAPI, data['email']);
      $.ajax({
        url: uberAPI,
        data: uberData,
        success: function(response) {
          var uberTime = parseInt(response.time) * 1000;
          app.logAPI(mapsAPI, data['email']);
          $.ajax({
            url: mapsAPI,
            data: mapsData,
            success: function(response) {
              // console.log(response);
              var mapsTime = parseInt(response.time) * 1000;
              var maxMapsTimeVariation = 3600000;
              remainingTime = remainingTime - uberTime - mapsTime - maxMapsTimeVariation;
              if (remainingTime > 0) {
                setTimeout(apiCalls, remainingTime);
              } else {
                $.ajax({
                  url: emailAPI,
                  data: emailData,
                  success: function(response) {
                    alert('Email Sent'); 
                  }
                });
              }
            }
          });
        }
      });
    }
    apiCalls();
    return false;
  });

  window.app = app;

}(this, this.document, jQuery));
