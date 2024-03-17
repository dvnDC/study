using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Forms;

using IOPath = System.IO.Path;

namespace WpfApp1
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {

        public MainWindow()
        {
            InitializeComponent();
        }

        private void OpenFolder_Click(object sender, RoutedEventArgs e)
        {
            using (var dlg = new FolderBrowserDialog())
            {
                dlg.Description = "Select a folder";
                if (dlg.ShowDialog() == System.Windows.Forms.DialogResult.OK)
                {
                    string selectedPath = dlg.SelectedPath;
                    LoadDirectoryStructure(selectedPath);
                }
            }
        }



        private void OpenFile_Click(object sender, RoutedEventArgs e)
        {
            // Zakładając, że Tag TreeViewItem zawiera ścieżkę do pliku
            if (FoldersTreeView.SelectedItem is TreeViewItem selectedItem && selectedItem.Tag is string filePath)
            {
                // Otwórz plik i wykonaj wymaganą logikę
                DisplayFileContent(filePath);
            }
        }


        private void LoadDirectoryStructure(string path)
        {
            var rootItem = new TreeViewItem
            {
                Header = IOPath.GetFileName(path),
                Tag = path
            };

            FillTreeViewItemWithFileSystemEntries(rootItem, path);
            FoldersTreeView.Items.Clear();
            FoldersTreeView.Items.Add(rootItem);
            rootItem.ExpandSubtree(); // Opcjonalnie, rozwiń wszystkie elementy
        }

        private void FillTreeViewItemWithFileSystemEntries(TreeViewItem item, string path)
        {
            foreach (var directoryPath in Directory.GetDirectories(path))
            {
                var subItem = new TreeViewItem
                {
                    Header = IOPath.GetFileName(directoryPath),
                    Tag = directoryPath
                };

                // Rekurencyjne dodawanie folderów
                FillTreeViewItemWithFileSystemEntries(subItem, directoryPath);
                item.Items.Add(subItem);
            }

            foreach (var filePath in Directory.GetFiles(path))
            {
                var subItem = new TreeViewItem
                {
                    Header = IOPath.GetFileName(filePath),
                    Tag = filePath
                };

                // Tworzenie nowego menu kontekstowego dla każdego pliku
                var fileContextMenuItem = new MenuItem { Header = "Open" };
                fileContextMenuItem.Click += (sender, args) =>
                {
                    var menuItem = sender as MenuItem;
                    // Użyj bezpośrednio Tag z menuItem do przechowywania ścieżki pliku
                    if (menuItem.Tag != null)
                    {
                        var fileToOpen = menuItem.Tag.ToString();
                        DisplayFileContent(fileToOpen);
                    }
                };
                // Przypisanie ścieżki pliku do Tag MenuItem
                fileContextMenuItem.Tag = filePath;

                var contextMenu = new ContextMenu();
                contextMenu.Items.Add(fileContextMenuItem);
                subItem.ContextMenu = contextMenu;

                item.Items.Add(subItem);
            }
        }


        private void DisplayFileContent(string filePath)
        {
            using (var textReader = System.IO.File.OpenText(filePath))
            {
                string text = textReader.ReadToEnd();
                FileContentTextBlock.Text = text;
            }
        }


        private void Exit_Click(object sender, RoutedEventArgs e)
        {
            this.Close(); // Zamknięcie bieżącego okna
        }

        private void DeleteMenuItem_Click(object sender, RoutedEventArgs e)
        {
            if (FoldersTreeView.SelectedItem is TreeViewItem selectedItem)
            {
                string path = selectedItem.Tag.ToString();
                if (File.Exists(path))
                {
                    File.Delete(path);
                }
                else if (Directory.Exists(path))
                {
                    Directory.Delete(path, recursive: true);
                }
                var parent = selectedItem.Parent as TreeViewItem;
                parent.Items.Remove(selectedItem);
            }
        }

        private void CreateMenuItem_Click(object sender, RoutedEventArgs e)
        {
            if (FoldersTreeView.SelectedItem is TreeViewItem selectedItem)
            {
                var createDialog = new CreateDialog();
                if (createDialog.ShowDialog() == true)
                {
                    try
                    {
                        string parentPath = selectedItem.Tag.ToString();
                        string newPath = IOPath.Combine(parentPath, createDialog.CreatedName);

                        if (createDialog.IsFile)
                        {
                            File.Create(newPath).Close(); // Close immediately after creating to release the handle
                            File.SetAttributes(newPath, createDialog.CreatedAttributes);
                        }
                        else
                        {
                            Directory.CreateDirectory(newPath);
                            File.SetAttributes(newPath, createDialog.CreatedAttributes);
                        }

                        var newItem = new TreeViewItem
                        {
                            Header = createDialog.CreatedName,
                            Tag = newPath
                        };

                        selectedItem.Items.Add(newItem);
                        selectedItem.ExpandSubtree();
                    }
                    catch (Exception ex)
                    {
                        System.Windows.MessageBox.Show($"Error creating file or directory: {ex.Message}", "Error", MessageBoxButton.OK, MessageBoxImage.Error);
                    }
                }
            }
        }

    }
}
