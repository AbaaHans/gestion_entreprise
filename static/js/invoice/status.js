export function initializeStatusUpdates() {
    const statusSelects = document.querySelectorAll('.status-select');
    
    statusSelects.forEach(select => {
        select.addEventListener('click', (e) => {
            e.preventDefault();
            showStatusModal(select);
        });
    });
}

function showStatusModal(select) {
    const invoiceId = select.dataset.invoiceId;
    const currentStatus = select.value;
    const statusChoices = JSON.parse(select.dataset.choices);
    
    const modal = createStatusModal(statusChoices, currentStatus, async (newStatus) => {
        const success = await updateInvoiceStatus(invoiceId, newStatus);
        if (success) {
            select.value = newStatus;
            select.textContent = statusChoices[newStatus];
            select.className = `btn status-select ${getStatusClass(newStatus)}`;
            modal.remove();
        }
    });
    
    document.body.appendChild(modal);
    modal.style.display = 'block';
}

function createStatusModal(choices, currentStatus, onSelect) {
    const modal = document.createElement('div');
    modal.className = 'modal fade show';
    modal.style.display = 'block';
    modal.style.backgroundColor = 'rgba(0,0,0,0.5)';
    modal.innerHTML = `
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Modifier le statut</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <div class="list-group">
                        ${Object.entries(choices).map(([value, label]) => `
                            <button class="list-group-item list-group-item-action status-choice ${getStatusClass(value)}" 
                                    data-value="${value}">
                                ${label}
                            </button>
                        `).join('')}
                    </div>
                </div>
            </div>
        </div>
    `;

    // Event listeners
    modal.querySelector('.btn-close').addEventListener('click', () => modal.remove());
    modal.querySelectorAll('.status-choice').forEach(choice => {
        choice.addEventListener('click', () => {
            onSelect(choice.dataset.value);
        });
    });

    // Close modal when clicking outside
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.remove();
        }
    });

    return modal;
}

async function updateInvoiceStatus(invoiceId, status) {
    try {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const response = await fetch(`/invoices/${invoiceId}/update-status/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken
            },
            body: `status=${status}`
        });
        
        const data = await response.json();
        return data.status === 'success';
    } catch (error) {
        console.error('Erreur lors de la mise à jour du statut:', error);
        return false;
    }
}

function getStatusClass(status) {
    const classes = {
        'draft': 'btn-warning',
        'sent': 'btn-info',
        'paid': 'btn-success',
        'cancelled': 'btn-danger'
    };
    return classes[status] || 'btn-secondary';
}