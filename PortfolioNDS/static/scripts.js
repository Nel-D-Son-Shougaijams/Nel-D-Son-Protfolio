// -------------------------JAVASCIRPT-------------------------
// -------------------------JAVASCIRPT-------------------------
const contactModalBtn = document.getElementById("Contact-Button")
const closeContactModal = document.getElementById("Close-Contact-Modal")
const contactModal = document.getElementById("contact")

contactModalBtn.addEventListener("click", () => {
    contactModal.style.display = "block"
})
closeContactModal.addEventListener("click", () => {
    contactModal.style.display = "none"
})