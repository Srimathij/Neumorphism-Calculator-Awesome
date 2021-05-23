 <script>
        function val(result) {
            form.display.value = form.display.value + result;
        }

        function calculate() {
            if (form.display.value == "") { // If user will enter '=' button without entering any number then we'll show him an alert
                alert("Enter the correct number & operators please!!!");
            } else {
                form.display.value = eval(form.display.value)
            }
        }
        var btn = form.veql;
        btn.addEventListener('dblclick', function() {
            form.display.value = ""; // If user will click '=' button once, screen will be cleared
        })
    </script>
