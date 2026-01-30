import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MatCard, MatCardHeader, MatCardTitle, MatCardContent, MatCardFooter } from "@angular/material/card";
import { MatFormField, MatLabel } from "@angular/material/form-field";
import { CommonModule } from '@angular/common';
import { MatInput } from '@angular/material/input';
import { MatButton } from '@angular/material/button';
import { MatTable, MatTableModule } from '@angular/material/table';

@Component({
  selector: 'app-wizard',
  templateUrl: './wizard.html',
  styleUrls: ['./wizard.scss'],
  standalone: true,
  imports: [
    CommonModule,
    MatCard, 
    MatCardHeader, 
    MatCardTitle, 
    MatCardContent, 
    MatCardFooter,
    MatFormField, 
    MatLabel, 
    MatInput,
    MatButton,
    MatTable,
    MatTableModule,
  ]
})
export class WizardComponent {

  actors: string[] = ['United States of America', 'People\'s Republic of China'];
  step: number = 1;

  constructor(private http: HttpClient) {}

  addActor(actor: string) {
    if (actor) {
      this.actors.push(actor);
    }
  }

  deleteActor(index: number) {
    this.actors.splice(index, 1);
  }

  nextStep() {
    this.step++;
  }

  previousStep() {
    this.step--;
  }

  submit() {
    this.http.post('http://localhost:5000/api/v1/generate', { actors: this.actors })
      .subscribe(response => {
        console.log(response);
      });
  }
}
