unit ReadFDF;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Xml.xmldom, Xml.XMLIntf, Vcl.StdCtrls,
  Xml.Win.msxmldom, Xml.XMLDoc;

type
  TForm1 = class(TForm)
    XMLDocument1: TXMLDocument;
    Button1: TButton;
    procedure Button1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}

procedure TForm1.Button1Click(Sender: TObject);
var
 i,j,k:integer;
 tempNode,tempNode1,tempNode2 : IXMLNode;
 nm,nm1,nm2:string;
 hdr:string;
 Qaree:string;
 myFile : TextFile;
begin
  AssignFile(myFile, 'H:\temp\W.txt');
  ReWrite(myFile);
  xmldocument1.filename:='H:\temp\W.xml';
  xmldocument1.Active := true;
   Qaree:='W';
   hdr:='Qaree,id,page,color,startX,StartY,EndX,EndY,RectX1,RectY1,RectX2,RectY2';
   WriteLn(myfile,hdr);
  for i := 0 to xmldocument1.ChildNodes.Count - 1 do begin

              tempNode := xmldocument1.ChildNodes.Get(i);

              nm:=tempNode.NodeName;

              if (tempNode.HasChildNodes) then // Has childs ?
              begin
                 for j := 0 to tempNode.ChildNodes.Count - 1 do // Gets child nodes
                 begin
                 tempnode1:=tempNode.ChildNodes.Get(j);
                 if tempnode1.HasAttribute('color') then
                   showmessage(tempnode1.attributes['color']);
    //             if (tempNode1.IsTextElement) then
                        nm1:=TempNode1.NodeName;
                if (tempNode1.HasChildNodes) then // Has childs ?
                begin
                   for k := 0 to tempNode1.ChildNodes.Count - 1 do // Gets child nodes
                   begin
                     tempNode2:=tempNode1.ChildNodes.Get(k);

                     if tempnode2.nodename='line' then
                       begin
                        nm2:='';
                        try
                          nm2:='"'+Qaree+'","'+tempNode2.Attributes['name']+'",'+tempNode2.Attributes['page']+',"'+tempNode2.Attributes['color']+'",'+tempNode2.Attributes['start']+','+tempNode2.Attributes['end']+','+tempNode2.Attributes['rect'];
                          WriteLn(myfile,nm2);
                        except
                        end;
                       end;
                   end;

                end;
                 end;

              end;

          end;
  CloseFile(myFile);
  showmessage('Done');
end;

end.
