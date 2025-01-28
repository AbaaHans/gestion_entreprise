// Calculs liés aux factures
export function calculateLineTotal(quantity, unitPrice) {
    return (parseFloat(quantity) || 0) * (parseFloat(unitPrice) || 0);
}

export function calculateGrandTotal(rows) {
    return rows.reduce((total, row) => {
        const quantity = row.querySelector('[name$="-quantity"]').value;
        const unitPrice = row.querySelector('[name$="-unit_price"]').value;
        return total + calculateLineTotal(quantity, unitPrice);
    }, 0);
}