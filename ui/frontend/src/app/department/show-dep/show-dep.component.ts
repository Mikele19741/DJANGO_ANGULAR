import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-show-dep',
  templateUrl: './show-dep.component.html',
  styleUrls: ['./show-dep.component.css']
})
export class ShowDepComponent implements OnInit {
  DepartmentList: any=[];
  ModalTitle: string="";
  ActivateAddEditDepComp:boolean=false;
  dep:any;
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
 
  addClick()
  {
      this.dep={
        DepartmentId:0,
        DepartmentName:""

      }
      this.ModalTitle="Add Department";
      this.ActivateAddEditDepComp=true;

  }
  closeClick()
  {
      this.ActivateAddEditDepComp=false;
      this.refreshDepList();
  }
}
