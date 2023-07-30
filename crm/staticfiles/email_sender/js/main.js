window.onload = function() {
    var emailInput = document.querySelector('input[name="email"]');
    var nameInput = document.querySelector('input[name="name"]');

    emailInput.addEventListener('paste', function(e) {
        e.preventDefault();
        expandInputs(e, 'email');
    });

    nameInput.addEventListener('paste', function(e) {
        e.preventDefault();
        expandInputs(e, 'name');
    });

    function expandInputs(e, fieldType) {
        var pasteData = e.clipboardData.getData('text');
        var dataArr = pasteData.split(/\s+/);

        var inputDiv = document.getElementById(fieldType + 'Inputs');
        for (var i = 0; i < dataArr.length; i++) {
            var newInput = document.createElement("input");
            newInput.type = "text";
            newInput.name = fieldType;
            newInput.value = dataArr[i];
            inputDiv.appendChild(newInput);
        }
    }
}