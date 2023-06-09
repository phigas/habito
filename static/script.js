document.addEventListener('DOMContentLoaded', function() {
    var divs = document.getElementsByClassName('daily-button');
    
    for (var i = 0; i < divs.length; i++) {
      divs[i].addEventListener('click', function() {
        // Perform desired actions when the div is clicked
        if (!this.classList.contains('deactivated')) {
            this.classList.toggle('clicked');
            this.classList.toggle('unclicked');
        }
        
      });
    }
  });