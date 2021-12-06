$(document).ready(function () {

    // {{test}} error
    // console.log(test) error
    console.log(URL)
    console.log(CSRF_TOKEN)


    $("#in_text").on("input", function () {

        // alert($(this).val()); 
        send_ajax($(this).val())
    });

    function send_ajax(input_data) {
        data = {
            'csrfmiddlewaretoken': CSRF_TOKEN,

        };
        data['text'] = input_data

        $.ajax({
            type: 'POST',
            // url: "http://127.0.0.1:8000/main/db_temp/",
            // url: "/main/db_temp/",
            url: URL,
            dataType: 'json',
            data: data,
            success: function (res) {
                console.log(res);
                show_persons(res)
            }
        });
    }

    function show_persons(data) {
        my_ul_tag = $('#mu_ul')
        my_ul_tag.empty()
        if (data['persons']) {
            for (const [key, value] of Object.entries(data['persons'])) {
                console.log("*", key, value);
                var li = document.createElement("li");
                var span1 = document.createElement("span");
                span1.append(value)
                li.append(span1)
                my_ul_tag.append(li)
            }

        } else {
            my_ul_tag.append()
        }

    }
});