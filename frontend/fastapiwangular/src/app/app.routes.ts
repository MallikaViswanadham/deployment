import { Routes } from '@angular/router';
import { Display } from './components/display/display';


export const routes: Routes = [
    { path: '', redirectTo: 'display', pathMatch: 'full' },
    { path: 'display', component: Display },
];
