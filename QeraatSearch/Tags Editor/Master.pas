unit Master;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants,
  System.Classes, Vcl.Graphics, Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Data.DB,
  Vcl.Grids, Vcl.DBGrids, Vcl.Bind.Grid, System.Rtti, System.Bindings.Outputs,
  Vcl.Bind.Editors, Data.Bind.EngExt, Vcl.Bind.DBEngExt, Data.Bind.Components,
  Data.Bind.Grid, Data.Bind.DBScope, Math, Vcl.ExtCtrls;

type
  TMasterF = class(TForm)
    BindSourceDB1: TBindSourceDB;
    StringGridBindSourceDB1: TStringGrid;
    LinkGridToDataSourceBindSourceDB1: TLinkGridToDataSource;
    BindingsList1: TBindingsList;
    BindSourceDB2: TBindSourceDB;
    StringGridBindSourceDB2: TStringGrid;
    LinkGridToDataSourceBindSourceDB2: TLinkGridToDataSource;
    Splitter1: TSplitter;
    procedure FormCreate(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  MasterF: TMasterF;

implementation

{$R *.dfm}

uses DM;

procedure AutoFitStringGridColumns(Grid: TStringGrid);
var
  i, j: Integer;
  MaxWidth: Integer;
  CellText: string;
begin
  for i := 0 to Grid.ColCount - 1 do
  begin
    MaxWidth := 0; // Reset the max width for the current column
    for j := 0 to Grid.RowCount - 1 do
    begin
      CellText := Grid.Cells[i, j];
      // Calculate the width needed for the cell text
      MaxWidth := Max(MaxWidth, Grid.Canvas.TextWidth(CellText));
    end;
    // Set the column width, adding some extra padding
    Grid.ColWidths[i] := MaxWidth + 10; // Adjust padding as necessary
  end;
end;

procedure TMasterF.FormCreate(Sender: TObject);
begin
  AutoFitStringGridColumns(StringGridBindSourceDB1);
  AutoFitStringGridColumns(StringGridBindSourceDB2);
end;

end.
