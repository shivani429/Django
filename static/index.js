// {% block javascript %}
<script>
    $("#friend-form").submit(function (e){
        // preventing from page reload and default actions
        e.preventDefault()};
        // serialize the data for sending the form data.
        var serializedData = $(this).serialize();
        // make POST ajax call
        $.ajax({{
            type: 'POST',
            url: "{% url 'post' %}",
            data: serializedData,
            success: function (response) {
                // on successfull creating object
                // 1. clear the form.
                $("#friend-form").trigger('reset');
                // 2. focus to nickname input 
                $("#id_nick_name").focus();

                // display the newly friend to table.
                var instance = JSON.parse(response["instance"]);
                var fields = instance[0]["fields"];
                $("#my_friends tbody").prepend(
                    `<tr>
                    <td>${fields["nick_name"]||""}</td>
                    <td>${fields["first_name"]||""}</td>
                    <td>${fields["last_name"]||""}</td>
                    <td>${fields["likes"]||""}</td>
                    <td>${fields["dob"]||""}</td>
                    <td>${fields["lives_in"]||""}</td>
                    </tr>`
                )
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        }   
    })
</script>
// {% endblcok javascript %}
