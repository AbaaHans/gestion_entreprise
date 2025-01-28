// Fonction pour calculer le total d'une ligne
function calculateLineTotal(row) {
    const quantity = parseFloat(row.querySelector('[name$="-quantity"]').value) || 0;
    const unitPrice = parseFloat(row.querySelector('[name$="-unit_price"]').value) || 0;
    return quantity * unitPrice;
}

// Fonction pour mettre à jour les prix depuis le produit sélectionné
async function updatePriceFromProduct(selectElement) {
    const row = selectElement.closest('.invoice-item');
    const productId = selectElement.value;
    const unitPriceInput = row.querySelector('[name$="-unit_price"]');
    const descriptionInput = row.querySelector('[name$="-description"]');
    
    if (productId) {
        const response = await fetch(`/api/products/${productId}/`);
        const product = await response.json();
        unitPriceInput.value = product.price;
        descriptionInput.value = product.name;
        updateTotals();
    }
}

// Fonction pour mettre à jour les prix depuis le service sélectionné
async function updatePriceFromService(selectElement) {
    const row = selectElement.closest('.invoice-item');
    const serviceId = selectElement.value;
    const unitPriceInput = row.querySelector('[name$="-unit_price"]');
    const descriptionInput = row.querySelector('[name$="-description"]');
    
    if (serviceId) {
        const response = await fetch(`/api/services/${serviceId}/`);
        const service = await response.json();
        unitPriceInput.value = service.price;
        descriptionInput.value = service.name;
        updateTotals();
    }
}

// Fonction pour mettre à jour tous les totaux
function updateTotals() {
    const rows = document.querySelectorAll('.invoice-item');
    let grandTotal = 0;
    
    rows.forEach(row => {
        const lineTotal = calculateLineTotal(row);
        grandTotal += lineTotal;
        
        // Mettre à jour l'affichage du total de la ligne
        const totalDisplay = row.querySelector('.line-total');
        if (totalDisplay) {
            totalDisplay.textContent = lineTotal.toFixed(2) + ' dhs';
        }
    });
    
    // Mettre à jour le total général
    const grandTotalDisplay = document.getElementById('grand-total');
    if (grandTotalDisplay) {
        grandTotalDisplay.textContent = grandTotal.toFixed(2) + ' dhs';
    }
}