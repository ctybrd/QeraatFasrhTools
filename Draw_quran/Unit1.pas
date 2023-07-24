unit Unit1;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls, Data.DB, Data.Win.ADODB,
  Vcl.Mask, JvExMask, JvToolEdit, Vcl.ExtCtrls,pngimage;

type
  TForm1 = class(TForm)
    src: TJvDirectoryEdit;
    dest: TJvDirectoryEdit;
    Button1: TButton;
    Label1: TLabel;
    Label2: TLabel;
    Lins: TADOQuery;
    Q: TRadioGroup;
    Image1: TImage;
    ADOQuery1: TADOQuery;
    ADOConnection1: TADOConnection;
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
 qk:string;
 i:integer;
 Stream : TMemoryStream;
 Image : TPngImage;
 x,y,width:integer;
 page_width,page_hi:integer;
begin
  case q.ItemIndex of
     0:qk:='K';
     1:qk:='B';
     2:qk:='J';
     3:qk:='B';
     4:qk:='WA';
     -1:exit;
  end;
  Image := TPngImage.Create;
  lins.Active:=false;
  Lins.SQL.Text:='select * from shmrly where qaree='''+qk+'''';
  for i := 2 to 522 do
     begin
        Lins.Active:=false;
        Lins.SQL.Text:='select * from shmrly where qaree='''+qk+''' and page_number='+inttostr(i);
        Lins.Active:=True;
       Stream := TMemoryStream.Create;
      try
        Stream.LoadFromFile(src.Text+'\'+inttostr(i)+'.png');
        Stream.Position := 0;
        image.LoadFromStream(Stream);
        page_width:=image.Width;
        page_hi:=image.Height;
        Lins.First;
        while not lins.Eof do
        begin
         if lins['color']='red' then
          image.Canvas.Pen.Color:=clred;
         if lins['color']='green' then
          image.Canvas.Pen.Color:=clGreen;
         if lins['color']='blue' then
            image.Canvas.Pen.Color:=clBlue;
          x:=trunc(page_width*lins.FieldByName('x').AsFloat);
          y:=trunc(page_hi*lins.FieldByName('y').AsFloat);
          width:=trunc(page_width*lins.FieldByName('width').AsFloat);
          image.Canvas.Pen.Width:=4;
          image.Canvas.Pen.mode:=pmMask;
//          image.Canvas.Pen.Mode:=pmXor;

          image.Canvas.MoveTo(x,y);
          image.Canvas.LineTo(x+width,y);
          application.ProcessMessages;
          lins.Next;
        end;
        Image1.Picture.Graphic:=image;
        image1.picture.SaveToFile(Dest.Text+'\'+inttostr(i)+'.png');

        //showmessage(inttostr(i));
      finally
        Stream.Free;
      end;
    end;
end;

end.
