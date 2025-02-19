unit Master;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants,
  System.Classes, Vcl.Graphics, Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Data.DB,
  Vcl.Grids, Vcl.DBGrids, Vcl.Bind.Grid, Math, Vcl.ExtCtrls, Data.Win.ADODB,
  Vcl.StdCtrls, System.StrUtils, Vcl.ComCtrls, Vcl.Buttons, System.UITypes,
  Vcl.WinXCtrls, Vcl.Mask, Vcl.DBCtrls;

type
  TMasterF = class(TForm)
    Spltr: TSplitter;
    HeadPnl: TPanel;
    HQ: TADOQuery;
    HDS: TDataSource;
    DDS: TDataSource;
    DQ: TADOQuery;
    DB: TADOConnection;
    CondPnl: TGridPanel;
    AyaEdt: TEdit;
    Label2: TLabel;
    SoraEdt: TEdit;
    Label3: TLabel;
    StatPnl: TGridPanel;
    StatusBar: TPanel;
    HCountPnl: TPanel;
    Qry: TADOQuery;
    ActnPnl: TGridPanel;
    DecFontPnl: TPanel;
    DecFontShp: TShape;
    DecFontBtn: TSpeedButton;
    IncFontPnl: TPanel;
    IncFontShp: TShape;
    IncFontBtn: TSpeedButton;
    HGrd: TDBGrid;
    DGrd: TDBGrid;
    DCountPnl: TPanel;
    RequeryPnl: TPanel;
    RequeryShp: TShape;
    RequeryBtn: TSpeedButton;
    HQsora: TIntegerField;
    HQaya: TIntegerField;
    HQsub_subject: TWideMemoField;
    HQqarees: TWideMemoField;
    HQqareesrest: TWideMemoField;
    HQwordindex: TIntegerField;
    DQsurah: TIntegerField;
    DQayah: TIntegerField;
    DQword: TWideMemoField;
    DQnextword: TWideMemoField;
    DQwordindex: TIntegerField;
    SearchBtn: TButton;
    procedure FormCreate(Sender: TObject);
    procedure DDSDataChange(Sender: TObject; Field: TField);
    procedure DBAfterConnect(Sender: TObject);
    procedure IncFontBtnClick(Sender: TObject);
    procedure DecFontBtnClick(Sender: TObject);
    procedure HGrdColumnMoved(Sender: TObject; FromIndex, ToIndex: Integer);
    procedure DGrdColumnMoved(Sender: TObject; FromIndex, ToIndex: Integer);
    procedure HDSDataChange(Sender: TObject; Field: TField);
    procedure ActnPnlDblClick(Sender: TObject);
    procedure RequeryBtnClick(Sender: TObject);
    procedure SearchBtnClick(Sender: TObject);
    procedure FormKeyDown(Sender: TObject; var Key: Word; Shift: TShiftState);
    procedure DGrdDrawColumnCell(Sender: TObject; const Rect: TRect;
      DataCol: Integer; Column: TColumn; State: TGridDrawState);
    procedure DGrdDblClick(Sender: TObject);
    procedure FormClose(Sender: TObject; var Action: TCloseAction);
  private
    function AddAnd(Txt: String): String;
    procedure WideMemoGetText(Sender: TField; var Text: string;
      DisplayText: Boolean);
    procedure WideMemoSetText(Sender: TField; const Text: string);
    procedure AssignWideMemoFieldEvents(Qry: TADOQuery);
    { Private declarations }
  public
    { Public declarations }
  end;

var
  MasterF: TMasterF;
  Pth: String;
  SqlH, WhrH, OrdrH: string;
  SqlD, WhrD, OrdrD: string;

implementation

{$R *.dfm}

procedure TMasterF.FormClose(Sender: TObject; var Action: TCloseAction);
begin
  HGrd.Columns.SaveToFile('HGrd.ini');
  DGrd.Columns.SaveToFile('DGrd.ini');
end;

procedure TMasterF.FormCreate(Sender: TObject);
begin
  Pth := ExtractFileDir(
    ExtractFileDir(ExtractFileDir(
    ExtractFileDir(Application.ExeName)))) + '\qeraat_data_simple.db';
  StatusBar.Caption := Pth;

  DB.Connected := False;
  DB.ConnectionString := 'Provider=MSDASQL.1;Driver=SQLite3 ODBC Driver;'
    + 'Database=' + Pth + ';';

  try
    DB.Connected := True;
  except on e: Exception do
    ShowMessage('Error: ' + e.Message);
  end;
end;

procedure TMasterF.FormKeyDown(Sender: TObject; var Key: Word;
  Shift: TShiftState);
begin
  if Key = VK_RETURN then
  begin
    SearchBtn.Click;
    Key := 0; // Prevent further processing of the Enter key
  end;
end;

procedure TMasterF.DBAfterConnect(Sender: TObject);
begin
  AssignWideMemoFieldEvents(HQ);
  AssignWideMemoFieldEvents(DQ);

  SqlH := 'SELECT sora, aya, sub_subject, qarees, qareesrest, wordindex '
    + 'FROM quran_data ';
  WhrH := 'Where sora = 100 ';
  OrdrH := 'order by sora, aya';
  HQ.SQL.Text := SqlH + WhrH + OrdrH;
  HQ.Open();

  SqlD := 'select surah, ayah, word, nextword, wordindex from wordsall ';
  WhrD := 'where surah = :sora and ayah = :aya ';
  OrdrD := 'order by surah, ayah, wordindex';
  DQ.SQL.Text := SqlD + WhrD + OrdrD;
  DQ.Open();

  if FileExists('HGrd.ini') then
    HGrd.Columns.LoadFromFile('HGrd.ini');
  if FileExists('DGrd.ini') then
    DGrd.Columns.LoadFromFile('DGrd.ini');
end;

{$Region 'Grid Positions'}
procedure TMasterF.HGrdColumnMoved(Sender: TObject; FromIndex,
  ToIndex: Integer);
begin
  HGrd.Columns.SaveToFile('HGrd.ini');
end;

procedure TMasterF.DGrdColumnMoved(Sender: TObject; FromIndex,
  ToIndex: Integer);
begin
  DGrd.Columns.SaveToFile('DGrd.ini');
end;

procedure TMasterF.DGrdDblClick(Sender: TObject);
begin
  HQ.Edit;
  HQwordindex.AsString := DQwordindex.AsString;
  HQ.Post;
end;

procedure TMasterF.DGrdDrawColumnCell(Sender: TObject; const Rect: TRect;
  DataCol: Integer; Column: TColumn; State: TGridDrawState);
begin
  if HQwordindex.AsString = DQwordindex.AsString then
  begin
    (Sender as TDBGrid).Canvas.Brush.Color := clYellow;
    (Sender as TDBGrid).Canvas.Font.Color := clBlack;
  end;

  (Sender as TDBGrid).DefaultDrawColumnCell(Rect, DataCol, Column, State);
end;
{$EndRegion}

{$Region 'Map Fields'}
procedure TMasterF.AssignWideMemoFieldEvents(Qry: TADOQuery);
var
  i: Integer;
  Field: TField;
begin
  for i := 0 to Qry.Fields.Count - 1 do
  begin
    Field := Qry.Fields[i];

    if Field.DataType = ftWideMemo then
    begin
      Field.OnGetText := WideMemoGetText;
      Field.OnSetText := WideMemoSetText;
    end;
  end;
end;

procedure TMasterF.WideMemoGetText(Sender: TField; var Text: string;
  DisplayText: Boolean);
begin
  Text := Sender.AsWideString;
end;

procedure TMasterF.WideMemoSetText(Sender: TField; const Text: string);
begin
  Sender.AsWideString := Text;
end;
{$EndRegion}

{$Region 'Filter Data'}
procedure TMasterF.RequeryBtnClick(Sender: TObject);
begin
  DBAfterConnect(DB);
end;

procedure TMasterF.SearchBtnClick(Sender: TObject);
var
  Fltr: String;
begin
  Fltr := '';

  if SoraEdt.Text <> '' then
  begin
    Fltr := 'sora = ' + SoraEdt.Text;
  end
  else
  begin
    SoraEdt.SetFocus;
    Exit;
  end;

  if AyaEdt.Text <> '' then
    Fltr := AddAnd(Fltr) + 'aya = ' + AyaEdt.Text;

  LockWindowUpdate(Handle);

  if Fltr = '' then
    Exit;

  try
    DQ.Close();
    HQ.Close();
    HQ.SQL.Text := SqlH + ' where ' + Fltr + ' ' + OrdrH;
    HQ.Open();
    DQ.Open();
  finally
    LockWindowUpdate(0);
    RedrawWindow(Handle, nil, 0, RDW_ERASE or RDW_FRAME or
      RDW_INVALIDATE or RDW_ALLCHILDREN);
  end;
end;

Function TMasterF.AddAnd(Txt: String): String;
begin
  Result := Ifthen(Txt <> '', Txt + ' And ', '');
end;
{$EndRegion}

{$Region 'Action Buttons'}
procedure TMasterF.ActnPnlDblClick(Sender: TObject);
begin
  ShowMessage(HQ.SQL.Text);
  ShowMessage(DQ.SQL.Text);
end;

procedure TMasterF.IncFontBtnClick(Sender: TObject);
begin
  Self.Font.Size := Self.Font.Size + 1;
  CondPnl.Height := CondPnl.Height + 3;
  HGrd.Font.Size := HGrd.Font.Size + 1;
  HGrd.TitleFont.Size := HGrd.Font.Size + 1;
  DGrd.Font.Size := DGrd.Font.Size + 1;
  DGrd.TitleFont.Size := HGrd.Font.Size + 1;
end;

procedure TMasterF.DecFontBtnClick(Sender: TObject);
begin
  Self.Font.Size := Self.Font.Size - 1;
  CondPnl.Height := CondPnl.Height - 3;
  HGrd.Font.Size := HGrd.Font.Size - 1;
  HGrd.TitleFont.Size := HGrd.Font.Size - 1;
  DGrd.Font.Size := DGrd.Font.Size - 1;
  DGrd.TitleFont.Size := HGrd.Font.Size - 1;
end;
{$EndRegion}

{$Region 'Record Count'}
procedure TMasterF.HDSDataChange(Sender: TObject; Field: TField);
begin
  if not HQ.IsEmpty then
    HCountPnl.Caption := Format('( %d : %d )', [HQ.RecNo, HQ.RecordCount])
  else
    HCountPnl.Caption := '( 0 : 0 )';
end;

procedure TMasterF.DDSDataChange(Sender: TObject; Field: TField);
begin
  if not DQ.IsEmpty then
    DCountPnl.Caption := Format('( %d : %d )', [DQ.RecNo, DQ.RecordCount])
  else
    DCountPnl.Caption := '( 0 : 0 )';
end;
{$EndRegion}

end.
