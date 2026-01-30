import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { WizardComponent } from "./wizard/wizard";

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, WizardComponent],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {
  protected readonly title = signal('Cyanide');
}
