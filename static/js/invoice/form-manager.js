// Gestion du formulaire de facture
import { updateAllTotals, handleProductSelection, handleServiceSelection } from './ui.js';

export function initializeFormHandlers() {
    // Gestionnaires d'événements pour les produits et services
    document.querySelectorAll('[name$="-product"]').forEach(select => {
        select.addEventListener('change', e => handleProductSelection(e.target));
    });

    document.querySelectorAll('[name$="-service"]').forEach(select => {
        select.addEventListener('change', e => handleServiceSelection(e.target));
    });

    // Gestionnaires pour les changements de quantité et prix
    document.querySelectorAll('[name$="-quantity"], [name$="-unit_price"]').forEach(input => {
        input.addEventListener('input', updateAllTotals);
    });
}

export function setupDynamicFormRows() {
    const addButton = document.getElementById('add-form');
    const itemsContainer = document.getElementById('invoice-items');
    
    if (addButton && itemsContainer) {
        addButton.addEventListener('click', () => addNewRow(itemsContainer));
        setupRowDeletion(itemsContainer);
    }
}

function addNewRow(container) {
    const formCount = container.children.length;
    const template = container.children[0].cloneNode(true);
    
    template.innerHTML = template.innerHTML.replace(/-\d+-/g, `-${formCount}-`);
    resetAndInitializeInputs(template);
    
    container.appendChild(template);
    document.getElementById('id_items-TOTAL_FORMS').value = formCount + 1;
    updateAllTotals();
}

function resetAndInitializeInputs(template) {
    template.querySelectorAll('input, select').forEach(input => {
        input.value = '';
        if (input.type !== 'hidden') {
            input.addEventListener('input', updateAllTotals);
        }
        if (input.tagName === 'SELECT') {
            const eventHandler = input.name.includes('-product') ? 
                handleProductSelection : handleServiceSelection;
            input.addEventListener('change', e => eventHandler(e.target));
        }
    });
}

function setupRowDeletion(container) {
    container.addEventListener('click', e => {
        if (e.target.classList.contains('remove-form')) {
            const item = e.target.closest('.invoice-item');
            if (container.children.length > 1) {
                item.remove();
                document.getElementById('id_items-TOTAL_FORMS').value = container.children.length;
                updateAllTotals();
            }
        }
    });
}