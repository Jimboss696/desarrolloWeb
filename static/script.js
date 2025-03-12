document.addEventListener("DOMContentLoaded", () => {
    const contactForm = document.getElementById("contact-form");

    if (contactForm) {
        contactForm.addEventListener("submit", async (event) => {
            event.preventDefault();

            let isValid = true;

            // Corregimos los IDs de los inputs (antes estaban incorrectos)
            const nameInput = document.getElementById("nombre");  // Antes: "name"
            const emailInput = document.getElementById("email");  // Antes: "email"
            const messageInput = document.getElementById("mensaje"); // Antes: "message"

            if (!nameInput || !emailInput || !messageInput) {
                console.error("Uno o más elementos del formulario no fueron encontrados.");
                return;
            }

            // Limpiar mensajes previos de error
            nameInput.classList.remove("is-invalid");
            emailInput.classList.remove("is-invalid");
            messageInput.classList.remove("is-invalid");

            // Validar nombre
            if (!nameInput.value.trim()) {
                nameInput.classList.add("is-invalid");
                isValid = false;
            }

            // Validar email con expresión regular
            if (!emailInput.value.trim().match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
                emailInput.classList.add("is-invalid");
                isValid = false;
            }

            // Validar mensaje
            if (!messageInput.value.trim()) {
                messageInput.classList.add("is-invalid");
                isValid = false;
            }

            // Si hay errores, no enviamos el formulario
            if (!isValid) return;

            // Enviar el formulario con Fetch
            const formData = new FormData(contactForm);

            try {
                const response = await fetch("/contacto", {  // Corregimos la ruta (antes: "/enviar_contacto")
                    method: "POST",
                    body: formData
                });

                if (response.ok) {
                    alert("Formulario enviado con éxito");
                    contactForm.reset();
                } else {
                    alert("Error al enviar el formulario");
                }
            } catch (error) {
                console.error("Error en la solicitud:", error);
                alert("Hubo un problema al enviar el formulario");
            }
        });
    }
});
