// Appels API pour les factures
export async function fetchProductDetails(productId) {
    const response = await fetch(`/api/products/${productId}/`);
    return response.json();
}

export async function fetchServiceDetails(serviceId) {
    const response = await fetch(`/api/services/${serviceId}/`);
    return response.json();
}

export async function updateInvoiceStatus(invoiceId, status, csrfToken) {
    const response = await fetch(`/invoices/${invoiceId}/update-status/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken
        },
        body: `status=${status}`
    });
    return response.json();
}