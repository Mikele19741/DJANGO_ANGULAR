import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-show-dep',
  templateUrl: './show-dep.component.html',
  styleUrls: ['./show-dep.component.css']
})
export class ShowDepComponent implements OnInit {
  DepartmentList: any=[];
  constructor(private service:SharedService) { }

  ngOnInit(): void {
    this.refreshDepList();
  }
  refreshDepList()
  {
    this.service.getDeptList().subscribe(data=>{
      this.DepartmentList=data;
    });
  }
}
