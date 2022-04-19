import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Cinema } from '../modules';
import { Cinemas } from '../cinemas';

@Component({
  selector: 'cinema.ts',
  templateUrl: './cinema.component.html',
  styleUrls: ['./cinema.component.css']
})
export class CinemaDetailComponent implements OnInit {
  cinema!: Cinemas
  constructor(private route:ActivatedRoute) { }

  ngOnInit(): void {
    this.getCinema()
  }
  getCinema(id: number){
     this.cinema = []
      }
}
