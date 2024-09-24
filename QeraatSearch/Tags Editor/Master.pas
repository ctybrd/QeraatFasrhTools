unit Master;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants,
  System.Classes, Vcl.Graphics, Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Data.DB,
  Vcl.Grids, Vcl.DBGrids, Vcl.Bind.Grid, System.Rtti, System.Bindings.Outputs,
  Vcl.Bind.Editors, Data.Bind.EngExt, Vcl.Bind.DBEngExt, Data.Bind.Components,
  Data.Bind.Grid, Data.Bind.DBScope, Math, Vcl.ExtCtrls, Data.Win.ADODB,
  Vcl.StdCtrls, System.StrUtils;

type
  TMasterF = class(TForm)
    HGrd: TStringGrid;
    DGrd: TStringGrid;
    Spltr: TSplitter;
    CountPnl: TPanel;
    Panel1: TPanel;
    HQ: TADOQuery;
    HQreading: TWideMemoField;
    HQcount: TIntegerField;
    HQsubject: TWideStringField;
    HQqarees: TWideStringField;
    HDS: TDataSource;
    DDS: TDataSource;
    DQ: TADOQuery;
    DQaya_index: TIntegerField;
    DQid: TIntegerField;
    DQsora: TIntegerField;
    DQaya: TIntegerField;
    DQsub_subject: TWideMemoField;
    DQqarees: TWideMemoField;
    DQreading: TWideMemoField;
    DQtags: TWideMemoField;
    DQpage_number1: TIntegerField;
    DQpage_number2: TIntegerField;
    DQreadingresult: TWideMemoField;
    DQqareesrest: TWideMemoField;
    DQcount_words: TIntegerField;
    DQsub_sno: TIntegerField;
    DQresultnew: TWideMemoField;
    DQwordsno: TIntegerField;
    DQDone: TIntegerField;
    BindSourceDB1: TBindSourceDB;
    BindingsList1: TBindingsList;
    LinkGridToDataSourceBindSourceDB1: TLinkGridToDataSource;
    BindSourceDB2: TBindSourceDB;
    LinkGridToDataSourceBindSourceDB2: TLinkGridToDataSource;
    DB: TADOConnection;
    CondPnl: TGridPanel;
    QuareesEdt: TEdit;
    Label1: TLabel;
    SubjectEdt: TEdit;
    Label2: TLabel;
    ReadingEdt: TEdit;
    Label3: TLabel;
    procedure FormCreate(Sender: TObject);
    procedure DDSDataChange(Sender: TObject; Field: TField);
    procedure DBAfterConnect(Sender: TObject);
    procedure HGrdDrawCell(Sender: TObject; ACol, ARow: Integer; Rect: TRect;
      State: TGridDrawState);
    procedure ReadingEdtChange(Sender: TObject);
  private
    Function FilterData(): String;
    function AddAnd(Txt: String): String;
    { Private declarations }
  public
    { Public declarations }
  end;

var
  MasterF: TMasterF;

implementation

{$R *.dfm}

procedure TMasterF.FormCreate(Sender: TObject);
var
  Pth: String;
begin
  Pth := ExtractFilePath(Application.ExeName) + 'qeraat_data_simple.db';

  DB.Connected := False;
  DB.ConnectionString := 'Provider=MSDASQL.1;Driver=SQLite3 ODBC Driver;'
    + 'Database=' + Pth + ';';

  try
    DB.Connected := True;
  except on e: Exception do
    ShowMessage('Error: ' + e.Message);
  end;
end;

procedure TMasterF.HGrdDrawCell(Sender: TObject; ACol, ARow: Integer;
  Rect: TRect; State: TGridDrawState);
var
  Text: string;
  TextWidth, TextHeight: Integer;
begin
  if ARow <> 0 then
    Exit;

  TStringGrid(Sender).Canvas.Brush.Color := $00FFD6D6;
  TStringGrid(Sender).Canvas.FillRect(Rect);
  Text := TStringGrid(Sender).Cells[ACol, ARow];

  TextWidth := TStringGrid(Sender).Canvas.TextWidth(Text);
  TextHeight := TStringGrid(Sender).Canvas.TextHeight(Text);

  TStringGrid(Sender).Canvas.TextRect(Rect,
    Rect.Left + (Rect.Width - TextWidth) div 2,
    Rect.Top + (Rect.Height - TextHeight) div 2, Text);
end;

procedure TMasterF.DBAfterConnect(Sender: TObject);
begin
  HQ.Open();
  DQ.Open();
end;

Function TMasterF.AddAnd(Txt: String): String;
begin
  Result := Ifthen(Txt <> '',Txt + ' And ','');
end;

procedure TMasterF.ReadingEdtChange(Sender: TObject);
var
  Fltr: String;
begin
  LockWindowUpdate(Handle);
  Fltr := FilterData();

  if Fltr = '' then
  begin
    HQ.Filtered := False;
    Exit;
  end;

  try
    HQ.Filtered := False;
    HQ.Filter := Fltr;
    HQ.Filtered := True;
  finally
    LockWindowUpdate(0);
    RedrawWindow(Handle, nil, 0, RDW_ERASE or RDW_FRAME or
      RDW_INVALIDATE or RDW_ALLCHILDREN);
  end;
end;

Function TMasterF.FilterData(): String;
begin
  if ReadingEdt.Text <> '' then
    Result := 'reading like ' + QuotedStr('%' + ReadingEdt.Text + '%');

  if SubjectEdt.Text <> '' then
    Result := AddAnd(Result)
      + 'subject like ' + QuotedStr('%' + SubjectEdt.Text + '%');

  if QuareesEdt.Text <> '' then
    Result := AddAnd(Result)
      + 'qarees like ' + QuotedStr('%' + QuareesEdt.Text + '%');
end;

procedure TMasterF.DDSDataChange(Sender: TObject; Field: TField);
begin
  if not DQ.IsEmpty then
    CountPnl.Caption := Format('( %d : %d )', [DQ.RecNo, DQ.RecordCount])
  else
    CountPnl.Caption := '( 0 : 0 )';
end;

end.
