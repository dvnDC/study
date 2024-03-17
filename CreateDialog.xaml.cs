using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace WpfApp1
{
    /// <summary>
    /// Interaction logic for CreateDialog.xaml
    /// </summary>
    public partial class CreateDialog : Window
    {
        public string CreatedName { get; private set; }
        public FileAttributes CreatedAttributes
        {
            get
            {
                FileAttributes attributes = default;
                if (ReadOnlyCheckBox.IsChecked == true) attributes |= FileAttributes.ReadOnly;
                if (HiddenCheckBox.IsChecked == true) attributes |= FileAttributes.Hidden;
                if (SystemCheckBox.IsChecked == true) attributes |= FileAttributes.System;
                return attributes;
            }
        }
        public bool IsFile => FileRadioButton.IsChecked == true;

        public CreateDialog()
        {
            InitializeComponent();
        }

        private void OkButton_Click(object sender, RoutedEventArgs e)
        {
            this.CreatedName = NameTextBox.Text;
            this.DialogResult = true;
        }

        private void CancelButton_Click(object sender, RoutedEventArgs e)
        {
            this.DialogResult = false;
        }
    }


}
