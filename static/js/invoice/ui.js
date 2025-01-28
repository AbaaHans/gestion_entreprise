// Gestion de l'interface utilisateur des factures
import { calculateLineTotal, calculateGrandTotal } from './calculations.js';
import { fetchProductDetails, fetchServiceDetails } from './api.js';

export function updateLineTotal(row) {
    const quantity = row.querySelector('[name$="-quantity"]').value;
    const unitPrice = row.querySelector('[name$="-unit_price"]').value;
    const total = calculateLineTotal(quantity, unitPrice);
    
    const totalDisplay = row.querySelector('.line-total');
    if (totalDisplay) {
        totalDisplay.textContent = total.toFixed(2) + ' €';
    }
}

export function updateAllTotals() {
    const rows = document.querySelectorAll('.invoice-item');
    const grandTotal = calculateGrandTotal(rows);
    
    rows.forEach(row => updateLineTotal(row));
    
    const grandTotalDisplay = document.getElementById('grand-total');
    if (grandTotalDisplay) {
        grandTotalDisplay.textContent = grandTotal.toFixed(2) + ' €';
    }
}

export async function handleProductSelection(selectElement) {
    const row = selectElement.closest('.invoice-item');
    const productId = selectElement.value;
    
    if (productId) {
        const product = await fetchProductDetails(productId);
        row.querySelector('[name$="-unit_price"]').value = product.price;
        row.querySelector('[name$="-description"]').value = product.name;
        updateAllTotals();
    }
}

export async function handleServiceSelection(selectElement) {
    const row = selectElement.closest('.invoice-item');
    const serviceId = selectElement.value;
    
    if (serviceId) {
        const service = await fetchServiceDetails(serviceId);
        row.querySelector('[name$="-unit_price"]').value = service.price;
        row.querySelector('[name$="-description"]').value = service.name;
        updateAllTotals();
    }
}