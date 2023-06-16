$(function() {
    var pinging = false;
    $('#results').html('');
    $('#enable_ping').on('click', function() {
        if (pinging) {
            pinging = false;
            $('#enable_ping').html('Enable Backend Ping');
            $('#results').html('');
        } else {
            pinging = true;
            $('#enable_ping').html('Disable Backend Ping');
            $('#results').html('');
        }
    });

    setInterval(function() {
        if (pinging) {
            $.ajax({
                url: "api/version",
                success: function(data) {
                    $('#results').html('Backend Version: <b>' + data.version + '</b>');
                },
                error: function () {
                    $('#results').html('<b>ERROR<b/>: Version Check Failed.');
                },
                timeout: 2000
            });
        }
    }, 5000);
});