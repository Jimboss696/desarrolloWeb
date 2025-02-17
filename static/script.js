document.addEventListener("DOMContentLoaded", () => {
    // Botón de alerta
    const alertButton = document.createElement("button");
    alertButton.textContent = "Haz clic aquí";
    alertButton.classList.add("btn", "btn-warning", "mt-3");
    document.querySelector("main").appendChild(alertButton);

    alertButton.addEventListener("click", () => {
        alert("¡Bienvenido a Black a White Society!");
    });

    // Validación del formulario de contacto
    const contactForm = document.getElementById("contact-form");
    if (contactForm) {
        contactForm.addEventListener("submit", (event) => {
            event.preventDefault();

            let isValid = true;
            const nameInput = document.getElementById("name");
            const emailInput = document.getElementById("email");
            const messageInput = document.getElementById("message");

            if (!nameInput.value.trim()) {
                nameInput.classList.add("is-invalid");
                isValid = false;
            } else {
                nameInput.classList.remove("is-invalid");
            }

            if (!emailInput.value.trim().match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
                emailInput.classList.add("is-invalid");
                isValid = false;
            } else {
                emailInput.classList.remove("is-invalid");
            }

            if (!messageInput.value.trim()) {
                messageInput.classList.add("is-invalid");
                isValid = false;
            } else {
                messageInput.classList.remove("is-invalid");
            }

            if (isValid) {
                alert("Formulario enviado con éxito");
                contactForm.reset();
            }
        });
    }
});