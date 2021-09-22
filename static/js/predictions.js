console.log('about');

var housing_cols = [];

fetch('/show_columns')
  .then(response => response.json())
  .then(feature_names => {
    console.log(feature_names);
    var user_input_html = ''
    feature_names.forEach(feature_name => {
      housing_cols.push(feature_name)
      user_input_html += `
        <input id = '${feature_name}' placeholder = '${feature_name}' style = 'width: 400px; text-align:center; margin-bottom:2px;'></input>
        <br>
        `
    });
    console.log(user_input_html);
    $('#text-input-boxes').html(user_input_html)
  });
function defaultValueButtonCicked(){

    document.querySelectorAll("input").forEach(e => e.value = parseInt(Math.random()*5 + 1 ));
}
function predictionsButtonClicked() {
    var typed_inputs = {}
    housing_cols.forEach(housing_col => {
        var user_input;
        console.log(housing_col)
        // if (d3.select(`#${housing_col}`).property('value')) {
        user_input = d3.select(`#${housing_col}`).property('value')
        // }
        // else {
        //     user_input = ""
        // }

        typed_inputs[housing_col] = user_input
    });
    console.log(typed_inputs)
    fetch('/generate_predictions', {
        method: 'POST', // or 'PUT'
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(typed_inputs),
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            var pred_div = d3.select("#prediction-text")
            pred_div.text(`$ ${data}`)
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}
