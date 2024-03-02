$(document).ready(function() {
    const setTime = () => {
        var date = new Date();
        $('#clock').html(
            String(date.getHours()).padStart(2, '0') + ':' + 
            String(date.getMinutes()).padStart(2, '0') + ':' + 
            String(date.getSeconds()).padStart(2, '0')
        );
    }

    setInterval(function() {
        setTime();
    }, 1);
});