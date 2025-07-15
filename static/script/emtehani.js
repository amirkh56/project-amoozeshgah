const text = "دوره های آموزشی کامپیوتری سره مینو";
    const heading = document.querySelector('.head-3');
    let index = 0;
    let reverse = false;
    function animate() {
      if (!reverse) {
        // تایپ حرف به حرف
        heading.textContent = text.slice(0, index + 1);
        index++;
        if (index === text.length) {
          reverse = true;
          setTimeout(animate, 1000); // مکث یک ثانیه بعد از تایپ کامل
          return;
        }
      } else {
        // پاک کردن متن حرف به حرف
        heading.textContent = text.slice(0, index - 1);
        index--; 
        if (index === 0) {
          reverse = false;
          setTimeout(animate, 500); // مکث نیم ثانیه بعد از پاک شدن کامل
          return;
        }
      }
      setTimeout(animate, 100);
    }
    animate();



    const hamburger = document.querySelector('.hamburger');
    const nav = document.querySelector('nav');
    const dropdownParents = document.querySelectorAll('li.has-dropdown > a');

    // باز و بسته کردن منوی موبایل
    hamburger.addEventListener('click', () => {
      const expanded = hamburger.getAttribute('aria-expanded') === 'true';
      hamburger.setAttribute('aria-expanded', !expanded);
      nav.classList.toggle('active');
    });

    // باز و بسته کردن زیرمنوها در موبایل
    dropdownParents.forEach(parentLink => {
      parentLink.addEventListener('click', (e) => {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          const li = parentLink.parentElement;
          const dropdown = li.querySelector('.dropdown');
          const isOpen = dropdown.classList.contains('open');

          // بستن همه زیرمنوهای دیگر
          dropdownParents.forEach(otherLink => {
            if (otherLink !== parentLink) {
              otherLink.parentElement.querySelector('.dropdown').classList.remove('open');
              otherLink.parentElement.classList.remove('open');
              otherLink.setAttribute('aria-expanded', 'false');
            }
          });

          if (isOpen) {
            dropdown.classList.remove('open');
            li.classList.remove('open');
            parentLink.setAttribute('aria-expanded', 'false');
          } else {
            dropdown.classList.add('open');
            li.classList.add('open');
            parentLink.setAttribute('aria-expanded', 'true');
          }
        }
      });
    });

    // برای دسترسی کیبوردی (باز کردن منو با اینتر یا اسپیس)
    hamburger.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        hamburger.click();
      }
    });

    dropdownParents.forEach(parentLink => {
      parentLink.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          parentLink.click();
        }
      });
    });



    
    const menu = document.getElementById("menu");
    hamburger.addEventListener("click", () => {
  const hamburger = document.getElementById("hamburger");
  const expanded = hamburger.getAttribute("aria-expanded") === "true";
  hamburger.setAttribute("aria-expanded", !expanded);
  menu.classList.toggle("show");
});

// باز و بسته کردن زیرمنو در موبایل
const parentItems = document.querySelectorAll("ul.menu > li");

parentItems.forEach(item => {
  item.addEventListener("click", () => {
    if (window.innerWidth <= 768) {
      item.classList.toggle("show-submenu");
      parentItems.forEach(other => {
        if (other !== item) {
          other.classList.remove("show-submenu");
        }
      });
    }
  });
});
