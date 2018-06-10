function find () {
  name = $('#query').val()
  $.ajax({
    type: 'POST',
    url: 'https://matchcareer.herokuapp.com/match',
    datatype: 'json',
    data: { name: name },
    success: function (data) {
      if (_.isEmpty(data)) {
        $('#results').html(
          '<div class="alert alert-danger" role="alert">' +
            '<h4 class="alert-heading">Error!</h4>' +
            '<p>Couldn\'t find a player named "' + name + '".</p>' +
          '</div>'
        )
      } else {
        var height = data['MyCareer']['Height']
        var primary = data['MyCareer']['Primary']
        var secondary = data['MyCareer']['Secondary']
        var position = data['MyCareer']['Position']

        var msg = 'Your suggested build is a ' + height + ', {' + primary +
                  ', ' + secondary + '} ' + position + '.'

        $('#results').html(
          '<div class="alert alert-success" role="alert">' +
            '<h4 class="alert-heading">Success!</h4>' +
            '<p>' + msg + '</p>' +
            '<hr>' +
            '<p class="mb-0">An attribute-by-attribute comparison is given below.</p>' +
          '</div>'
        )

        console.log(JSON.stringify(data))
      }
    },
    error: function (error) {
      console.log(error)
    }
  })
};

var index = [
  'Stephen Curry',
  'Karl-Anthony Towns',
  'Giannis Antetokounmpo'
]

$('#query').typeahead({ source: index })
