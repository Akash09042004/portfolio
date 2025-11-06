#refreshed
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
// Contact Form with Loading Spinner
// -----------------------------
const pages = document.querySelectorAll('.book-page.page-right');
const contactForm = document.querySelector('#contactForm');

contactForm.addEventListener('submit', async function(e) {
    e.preventDefault();

    const name = contactForm.name.value.trim();
    const email = contactForm.email.value.trim();
    const message = contactForm.message.value.trim();

    if (!name || !email || !message) {
        alert("Please fill all fields!");
        return;
    }

    // Spinner inside the submit button
    const submitBtn = contactForm.querySelector('.btn');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = "Sending...";
    submitBtn.disabled = true;

    // ✅ Use your Render backend URL here
    const backendURL = "https://portfolio-gqwn.onrender.com/contact";

    try {
        const response = await fetch(backendURL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, email, message })
        });

        const data = await response.json();

        if (response.ok) {
            alert(data.message || "Message sent successfully!");
            contactForm.reset();

            // Optional: Page flip animation after sending
            pages.forEach((page, index) => {
                setTimeout(() => {
                    page.classList.add('turn');
                    setTimeout(() => {
                        page.style.zIndex = 20 + index;
                    }, 500);
                }, (index + 1) * 200 + 100);
            });
        } else {
            alert(data.error || "Something went wrong. Try again.");
        }

    } catch (err) {
        console.error("Error sending message:", err);
        alert("Something went wrong. Try again.");
    } finally {
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
    }
});

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

