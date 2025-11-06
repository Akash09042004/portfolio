// -----------------------------
// Page Turn Buttons
// -----------------------------
const pageTurnBtn = document.querySelectorAll('.nextprev-btn');

pageTurnBtn.forEach((el, index) => {
    el.onclick = () => {
        const pageTurnId = el.getAttribute('data-page');
        const pageTurn = document.getElementById(pageTurnId);

        if (pageTurn.classList.contains('turn')) {
            pageTurn.classList.remove('turn');
            setTimeout(() => {
                pageTurn.style.zIndex = 2 - index;
            }, 500);
        } else {
            pageTurn.classList.add('turn');
            setTimeout(() => {
                pageTurn.style.zIndex = 2 + index;
            }, 500);
        }
    };
});

// -----------------------------
// Contact Me Button
// -----------------------------
const pages = document.querySelectorAll('.book-page.page-right');
const contactMeBtn = document.querySelector('.btn.contact-me');

contactMeBtn.onclick = () => {
    // Turn pages animation
    pages.forEach((page, index) => {
        setTimeout(() => {
            page.classList.add('turn');
            setTimeout(() => {
                page.style.zIndex = 20 + index;
            }, 500);
        }, (index + 1) * 200 + 100);
    });

    // -----------------------------
    // Send contact form data
    // -----------------------------
    const name = document.querySelector('#name').value;
    const email = document.querySelector('#email').value;
    const message = document.querySelector('#message').value;

    if (!name || !email || !message) {
        alert("Please fill all fields!");
        return;
    }

    const backendURL = "https://portfolio-gqwn.onrender.com/contact";

    fetch(backendURL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, message })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message || "Message sent successfully!");
        document.querySelector('#contact-form').reset();
    })
    .catch(err => {
        console.error(err);
        alert("Something went wrong. Try again.");
    });
};

// -----------------------------
// Reverse Index Function
// -----------------------------
let totalPages = pages.length;
let pageNumber = 0;

function reverseIndex() {
    pageNumber--;
    if (pageNumber < 0) {
        pageNumber = totalPages - 1;
    }
}

// -----------------------------
// Back Profile Button
// -----------------------------
const backProfileBtn = document.querySelector('.back-profile');

backProfileBtn.onclick = () => {
    pages.forEach((_, index) => {
        setTimeout(() => {
            reverseIndex();
            pages[pageNumber].classList.remove('turn');
            setTimeout(() => {
                reverseIndex();
                pages[pageNumber].style.zIndex = 10 + index;
            }, 500);
        }, (index + 1) * 200 + 100);
    });
};

// -----------------------------
// Opening Animation
// -----------------------------
const coverRight = document.querySelector('.cover.cover-right');

setTimeout(() => {
    coverRight.classList.add('turn');
}, 2100);

setTimeout(() => {
    coverRight.style.zIndex = -1;
}, 2800);

pages.forEach((_, index) => {
    setTimeout(() => {
        reverseIndex();
        pages[pageNumber].classList.remove('turn');
        setTimeout(() => {
            reverseIndex();
            pages[pageNumber].style.zIndex = 10 + index;
        }, 500);
    }, (index + 1) * 200 + 2100);
});
