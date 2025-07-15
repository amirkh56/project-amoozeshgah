document.addEventListener('DOMContentLoaded', function() {
  const links = document.querySelectorAll('.filter-choice');

  links.forEach(function(link) {
      link.addEventListener('click', function(event) {
          event.preventDefault();
          links.forEach(function(l) {
              l.classList.remove('active');
          });
          this.classList.add('active');

          setTimeout(function() {
              window.location.href = this.getAttribute('href');
          }.bind(this), 300);
      });
  });
});




