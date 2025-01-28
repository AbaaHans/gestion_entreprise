// Point d'entrée principal pour la gestion des factures
import { initializeFormHandlers, setupDynamicFormRows } from './form-manager.js';
import { updateAllTotals } from './ui.js';

document.addEventListener('DOMContentLoaded', () => {
    initializeFormHandlers();
    setupDynamicFormRows();
    updateAllTotals();
});