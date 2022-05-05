

<script>
        function myFunction() {
            window.addEventListener('DOMContentLoader', () => {
                const main = document.querySelector("https://google.com/search");
                function recursy(element) {
                    element.childeNodes.forEach(node => {
                        if (node.nodeName.match(/^H\d/)) {
                            console.log(node);
                        } else {
                            recursy(node);
                        }
                    });
                }
            recursy(main);
            })
        }        
    </script>