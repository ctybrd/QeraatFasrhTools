unit Master;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants,
  System.Classes, Vcl.Graphics, Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Data.DB,
  Vcl.Grids, Vcl.DBGrids, Vcl.Bind.Grid, Math, Vcl.ExtCtrls, Data.Win.ADODB,
  Vcl.StdCtrls, System.StrUtils, Vcl.ComCtrls, Vcl.Buttons, System.UITypes;

type
  TMasterF = class(TForm)
    Spltr: TSplitter;
    HeadPnl: TPanel;
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
    DB: TADOConnection;
    CondPnl: TGridPanel;
    QuareesEdt: TEdit;
    Label1: TLabel;
    SubjectEdt: TEdit;
    Label2: TLabel;
    ReadingEdt: TEdit;
    Label3: TLabel;
    StatPnl: TGridPanel;
    StatusBar: TPanel;
    HCountPnl: TPanel;
    Qry: TADOQuery;
    ActnPnl: TGridPanel;
    UpdPnl: TPanel;
    UpdShp: TShape;
    UpdateBtn: TSpeedButton;
    DecFontPnl: TPanel;
    DecFontShp: TShape;
    DecFontBtn: TSpeedButton;
    IncFontPnl: TPanel;
    IncFontShp: TShape;
    IncFontBtn: TSpeedButton;
    HGrd: TDBGrid;
    DGrd: TDBGrid;
    DCountPnl: TPanel;
    procedure FormCreate(Sender: TObject);
    procedure DDSDataChange(Sender: TObject; Field: TField);
    procedure DBAfterConnect(Sender: TObject);
    procedure ReadingEdtChange(Sender: TObject);
    procedure UpdateBtnClick(Sender: TObject);
    procedure IncFontBtnClick(Sender: TObject);
    procedure DecFontBtnClick(Sender: TObject);
    procedure HGrdColumnMoved(Sender: TObject; FromIndex, ToIndex: Integer);
    procedure DGrdColumnMoved(Sender: TObject; FromIndex, ToIndex: Integer);
    procedure HDSDataChange(Sender: TObject; Field: TField);
  private
    Function FilterData(): String;
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

implementation

{$R *.dfm}

procedure TMasterF.FormCreate(Sender: TObject);
var
  Pth: String;
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

procedure TMasterF.DBAfterConnect(Sender: TObject);
begin
  AssignWideMemoFieldEvents(HQ);
  AssignWideMemoFieldEvents(DQ);

  HQ.Open();
  DQ.Open();

  if FileExists('HGrd.ini') then
    HGrd.Columns.LoadFromFile('HGrd.ini');
  if FileExists('DGrd.ini') then
    DGrd.Columns.LoadFromFile('DGrd.ini');
end;

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

procedure TMasterF.UpdateBtnClick(Sender: TObject);
var
  SQL: String;
begin
  SQL := 'UPDATE quran_data ' +
    'SET resultnew = (Select a.resultnew ' +
    'FROM quran_data AS a ' +
    'WHERE NOT(a.resultnew IS NULL or a.resultnew = '''') ' +
    'AND a.sub_subject = quran_data.sub_subject ' +
    'AND a.reading = quran_data.reading) ' +
    'WHERE (quran_data.resultnew IS NULL or quran_data.resultnew='''')';

  Qry.SQL.Text := SQL;
  ShowMessage(SQL);

  if MessageDlg('Are you sure you want to update same records?',
    mtConfirmation, [mbYes, mbNo], 0) = mrYes then
  begin
    Qry.ExecSQL;
    HQ.Requery();
    DQ.Requery();
    ShowMessage('Done');
  end;
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

end.
